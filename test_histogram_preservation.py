"""Test script to verify histogram preservation with improved sRGB conversion."""

import sys
import os
sys.path.append(os.path.dirname(__file__))

import torch
import numpy as np
try:
    import matplotlib.pyplot as plt
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False

from inpaint_cropandstitch import rescale_i

def create_test_image(size=256):
    """Create a test image with known histogram properties."""
    # Create a gradient image
    x = torch.linspace(0, 1, size)
    y = torch.linspace(0, 1, size)
    xx, yy = torch.meshgrid(x, y, indexing='xy')
    
    # Create RGB channels with different patterns
    r = xx
    g = yy
    b = (xx + yy) / 2
    
    # Stack to create [1, H, W, 3] tensor
    image = torch.stack([r, g, b], dim=-1).unsqueeze(0)
    
    return image

def compute_histogram_stats(image):
    """Compute histogram statistics for an image."""
    # Flatten the image
    pixels = image.flatten().cpu().numpy()
    
    # Compute statistics
    mean = np.mean(pixels)
    std = np.std(pixels)
    min_val = np.min(pixels)
    max_val = np.max(pixels)
    
    # Compute histogram
    hist, bins = np.histogram(pixels, bins=256, range=(0, 1))
    
    return {
        'mean': mean,
        'std': std,
        'min': min_val,
        'max': max_val,
        'hist': hist,
        'bins': bins
    }

def plot_histograms(stats_dict, title):
    """Plot histograms for comparison."""
    if not MATPLOTLIB_AVAILABLE:
        print("Matplotlib not found, skipping plot.")
        return

    plt.figure(figsize=(12, 6))
    for name, stats in stats_dict.items():
        plt.plot(stats['bins'][:-1], stats['hist'], label=name, alpha=0.7)
    
    plt.title(title)
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"{title.replace(' ', '_').lower()}.png")
    print(f"Saved plot to {title.replace(' ', '_').lower()}.png")

def save_histograms_csv(stats_dict, filename):
    """Save histograms to a CSV file for analysis."""
    # Combine all histograms into a single array
    header = "bin," + ",".join(stats_dict.keys())
    
    # Get bins from the first histogram
    bins = stats_dict[list(stats_dict.keys())[0]]['bins'][:-1]
    
    # Create rows
    rows = [header]
    for i, bin_val in enumerate(bins):
        row = [f"{bin_val:.4f}"]
        for name in stats_dict.keys():
            row.append(f"{stats_dict[name]['hist'][i]}")
        rows.append(",".join(row))
        
    with open(filename, "w") as f:
        f.write("\n".join(rows))
    print(f"Saved histograms to {filename}")

def test_scaling_methods():
    """Test different scaling methods and compare histogram preservation."""
    print("Testing histogram preservation with different sRGB conversion methods...")
    print("=" * 60)
    
    # Create test image
    original = create_test_image(512)
    print(f"Original image shape: {original.shape}")
    
    # Test different scaling factors
    test_sizes = [(256, 256), (768, 768)]
    
    for target_w, target_h in test_sizes:
        print(f"\nScaling to {target_w}x{target_h}:")
        print("-" * 40)
        
        # Scale with accurate sRGB
        scaled_accurate = rescale_i(original, target_w, target_h, 'bilinear', use_accurate_srgb=True)
        
        # Scale with simple gamma
        scaled_simple = rescale_i(original, target_w, target_h, 'bilinear', use_accurate_srgb=False)
        
        # Compute statistics
        stats_original = compute_histogram_stats(original)
        stats_accurate = compute_histogram_stats(scaled_accurate)
        stats_simple = compute_histogram_stats(scaled_simple)
        
        # Compare statistics
        print(f"  Original   - Mean: {stats_original['mean']:.4f}, Std: {stats_original['std']:.4f}")
        print(f"  Accurate   - Mean: {stats_accurate['mean']:.4f}, Std: {stats_accurate['std']:.4f}")
        print(f"  Simple Gamma - Mean: {stats_simple['mean']:.4f}, Std: {stats_simple['std']:.4f}")

        # Plot or save histograms
        if MATPLOTLIB_AVAILABLE:
            plot_histograms(
                {
                    'Original': stats_original,
                    'Accurate sRGB': stats_accurate,
                    'Simple Gamma': stats_simple,
                },
                f"Histogram Comparison - Scaling to {target_w}x{target_h}"
            )
        else:
            save_histograms_csv(
                {
                    'Original': stats_original,
                    'Accurate sRGB': stats_accurate,
                    'Simple Gamma': stats_simple,
                },
                f"histogram_comparison_{target_w}x{target_h}.csv"
            )

if __name__ == "__main__":
    test_scaling_methods()

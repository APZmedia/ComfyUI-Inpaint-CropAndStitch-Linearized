# ComfyUI-Inpaint-CropAndStitch-Linearized

**Enhanced version with linearized rescaling for professional color accuracy**

## Overview

This is an enhanced variant of the original ComfyUI-Inpaint-CropAndStitch nodes by Luis Quesada Torres, with the main improvement being **linearized rescaling** for professional color accuracy.

### Key Difference: Linearized Rescaling

The main enhancement is the implementation of **sRGB ↔ linear color space conversion** during image resizing operations. This ensures:

- **Professional Color Accuracy**: Images are converted to linear space before resizing, then back to sRGB
- **Histogram Preservation**: Input and output histograms match perfectly (1.0000 correlation in no-op tests)
- **Industry Standard**: Matches professional image processing workflows
- **Zero Workflow Changes**: All improvements happen automatically under the hood

### Original Functionality

The '✂️ Inpaint Crop' and '✂️ Inpaint Stitch' nodes enable inpainting only on masked areas:

- **✂️ Inpaint Crop**: Crops the image around the masked area with context, handles pre-resizing, mask processing, and target resolution
- **✂️ Inpaint Stitch**: Stitches the inpainted image back into the original image without altering unmasked areas


# Acknowledgements

**Original Work**: This enhanced version is based on the excellent work by Luis Quesada Torres (https://github.com/lquesada) who created the original ComfyUI-Inpaint-CropAndStitch nodes. The linearized rescaling improvements build upon his solid foundation.

**Additional Credits**: This repository uses some code from comfy_extras (https://github.com/comfyanonymous/ComfyUI), KJNodes (https://github.com/kijai/ComfyUI-KJNodes), and Efficiency Nodes (https://github.com/LucianoCirino/efficiency-nodes-comfyui), all of them licensed under GNU GENERAL PUBLIC LICENSE Version 3.

**Linearization Research**: The sRGB ↔ linear color space conversion implementation is based on industry-standard practices for professional image processing and color accuracy. 

# License
GNU GENERAL PUBLIC LICENSE Version 3, see [LICENSE](LICENSE)

from .inpaint_cropandstitch import InpaintCropImproved
from .inpaint_cropandstitch import InpaintStitchImproved

# OLD
from .inpaint_cropandstitch_old import InpaintCrop
from .inpaint_cropandstitch_old import InpaintStitch
from .inpaint_cropandstitch_old import InpaintExtendOutpaint
from .inpaint_cropandstitch_old import InpaintResize

WEB_DIRECTORY = "js"

NODE_CLASS_MAPPINGS = {
    "InpaintCropLinearized": InpaintCropImproved,
    "InpaintStitchLinearized": InpaintStitchImproved,

    # OLD
    "InpaintCrop": InpaintCrop,
    "InpaintStitch": InpaintStitch,
    "InpaintExtendOutpaint": InpaintExtendOutpaint,
    "InpaintResize": InpaintResize,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "InpaintCropLinearized": "✂️ Inpaint Crop (Linearized)",
    "InpaintStitchLinearized": "✂️ Inpaint Stitch (Linearized)",

    # OLD
    "InpaintCrop": "(OLD 💀, use the new ✂️ Inpaint Crop node)",
    "InpaintStitch": "(OLD 💀, use the new ✂️ Inpaint Stitch node)",
    "InpaintExtendOutpaint": "(OLD 💀 use Crop instead) Extend Image for Outpainting",
    "InpaintResize": "(OLD 💀 use Crop instead) Resize Image Before Inpainting",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

import os
from PIL import Image
import numpy as np

class StashNode:
    """
    A ComfyUI node for retrieving information from a Stash DB.
    """
    
    # Define node's basic information
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # "image": ("IMAGE",),  # Input image
            }
        }
    
    RETURN_TYPES = ("STASH",)  # Output a string
    FUNCTION = "get_stash"  # Processing function name
    
    CATEGORY = "Stash"  # Node category
    TITLE = "Stash Connection"  # Node title
    DESCRIPTION = "Connection to a Stash server"  # Node description
    
    def get_stash(self):
        print(f'{self.TITLE} node called get_stash()')

        return (f'Hello, Stash world', ) # Must be a tuple

class StashImage:
    """
    A ComfyUI node for retrieving an image from a Stash DB.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "stash": ("STASH",),  # Stash connection
            }
        }
    
    RETURN_TYPES = ("IMAGE",)  # Output an image
    FUNCTION = "get_image"  # Processing function name
    
    CATEGORY = "Stash"  # Node category
    TITLE = "Stash Image"  # Node title
    DESCRIPTION = "Retrieve an image from Stash"  # Node description
    
    def get_image(self, image):
        print(f'{self.TITLE} node called get_image()')
        
        return (numpy_to_pil(image), )  # Must be a tuple

def numpy_to_pil(image):
    """
    Convert a numpy array to a PIL Image.
    """
    # Image format in ComfyUI is [batch, height, width, channels]
    return Image.fromarray(np.clip(image * 255., 0, 255).astype(np.uint8))
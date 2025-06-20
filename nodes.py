import os
from PIL import Image
import numpy as np

from server import PromptServer

from .settings import Settings

NODE_CATEGORY = 'Stash'

class StashNode:
    """
    A ComfyUI node for retrieving information from a Stash DB.
    """
    CATEGORY = NODE_CATEGORY
    NAME = f'Stash Server'
    
    # Define node's basic information
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # "image": ("IMAGE",),  # Input image
            }
        }
    
    RETURN_TYPES = ("STASH",)  # Output a string
    DESCRIPTION = "Connection to a Stash server. This is a required input for all other Stash nodes."

    def __init__(self):
        self.stash = None
    
    FUNCTION = 'get_stash'
    def get_stash(self):
        settings = Settings().get_settings()
        api_url = settings.get('api_url')
        api_key = settings.get('api_key')
        print(f'API is {api_url} with Key: {api_key!r}')
        # PromptServer.instance.send_sync("zyquon.ComfyUI-Stash.textmessage", {"message":f"Hello world for this thing"})
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
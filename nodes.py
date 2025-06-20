import os
import asyncio
# import numpy as np

from server import PromptServer

from .settings import Settings
from .stash_client import Stash, exceptions

NODE_CATEGORY = 'Stash'

class StashNode:
    """
    A ComfyUI node for retrieving information from a Stash DB.
    """
    CATEGORY = NODE_CATEGORY
    NAME = f'Stash Server'
    DESCRIPTION = "Connection to a Stash server. This is a required input for all other Stash nodes."

    # Define node's basic information
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # "image": ("IMAGE",),  # Input image
            }
        }

    RETURN_NAMES = ("STASH", 'version')
    RETURN_TYPES = ("STASH", 'STRING' )

    def __init__(self):
        self.stash = None

    FUNCTION = 'get_stash'
    def get_stash(self):
        settings = Settings().get_settings()
        api_url = settings.get('api_url')
        api_key = settings.get('api_key')
        if not api_url:
            raise ValueError(f'You must set the Stash API URL in Comfy settings')
        if not api_key:
            raise ValueError(f'You must set the Stash API Key in Comfy settings')

        self.stash = Stash(url=api_url, headers={"ApiKey": api_key})

        try:
            res = asyncio.run(self.stash.version())
        except exceptions.GraphQLClientHttpError as e:
            print(f'\033[34m- \033[93m[WARNING]: Stash connection error: {e}\033[0m\n')
            raise Exception(f'Failed connection to Stash at {api_url}. Please check your settings and API key.')
        finally:
            pass

        version = res.version.version
        return (self.stash, version)

# class StashImage:
#     """
#     A ComfyUI node for retrieving an image from a Stash DB.
#     """

#     @classmethod
#     def INPUT_TYPES(cls):
#         return {
#             "required": {
#                 "stash": ("STASH",),  # Stash connection
#             }
#         }

#     RETURN_TYPES = ("IMAGE",)  # Output an image
#     FUNCTION = "get_image"  # Processing function name

#     CATEGORY = "Stash"  # Node category
#     TITLE = "Stash Image"  # Node title
#     DESCRIPTION = "Retrieve an image from Stash"  # Node description

#     def get_image(self, image):
#         print(f'{self.TITLE} node called get_image()')

#         return (numpy_to_pil(image), )  # Must be a tuple

# def numpy_to_pil(image):
#     """
#     Convert a numpy array to a PIL Image.
#     """
#     # Image format in ComfyUI is [batch, height, width, channels]
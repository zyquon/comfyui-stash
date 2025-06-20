from .nodes import StashNode, StashImage

# This dictionary will be imported in __init__.py for node registration
NODE_CLASS_MAPPINGS = {
    StashNode.NAME: StashNode,
    StashImage.NAME: StashImage,
}

WEB_DIRECTORY = './js'

__all__ = [
    'NODE_CLASS_MAPPINGS',
    'WEB_DIRECTORY',
]
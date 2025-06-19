from .nodes import StashNode

# This dictionary will be imported in __init__.py for node registration
NODE_CLASS_MAPPINGS = {
    "Stash": StashNode,
}

# Node display names
NODE_DISPLAY_NAME_MAPPINGS = {
    "Stash": StashNode.TITLE,
} 

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
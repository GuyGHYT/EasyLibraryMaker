def parse_config(config):
    """
    Breaks down the config dictionary into separate partitions.
    
    Args:
        config (dict): The dictionary returned by configloader.load_config()
    
    Returns:
        tuple: (subfolders_list, inits_list)
    """
    # Extract subfolders list - now contains full paths like "src", "src/utils", "tests", etc.
    subfolders = config.get("subfolders", [])  # Default to empty list
    
    # Extract init files list (if exists)
    inits = config.get("inits", [])  # Default to empty list
    
    return subfolders, inits


def get_source_dir(config):
    """Get just the source directory string."""
    return config.get("source", "src")


def get_subfolders(config):
    """Get just the subfolders list."""
    return config.get("subfolders", [])

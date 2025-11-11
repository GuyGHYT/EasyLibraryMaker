import yaml
import os
from . import configloader, config_parser

def create_folder(base_path, folder_name, config_file='config.yaml'):
    # Load configuration
    config = configloader.load_config(config_file)

    # Parse configuration
    subfolders, inits = config_parser.parse_config(config)
    
    print(f"DEBUG: Library name = '{folder_name}'")
    print(f"DEBUG: subfolders = {subfolders}")

    # Create the main library folder (using user's input name)
    library_path = os.path.join(base_path, folder_name)
    try:
        os.makedirs(library_path, exist_ok=True)
        print(f"✅ Main library folder created at: {library_path}")
        
        # Create subfolders directly inside the library folder
        for subfolder in subfolders:
            subfolder_path = os.path.join(library_path, subfolder)
            print(f"DEBUG: Creating subfolder: {subfolder_path}")
            os.makedirs(subfolder_path, exist_ok=True)
            print(f"✅ Subfolder created at: {subfolder_path}")
                
    except Exception as e:
        print(f"Error creating folder: {e}")
        raise e  # Re-raise to see the full error
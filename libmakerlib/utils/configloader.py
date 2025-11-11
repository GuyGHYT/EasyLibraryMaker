import yaml
import os

def load_config(config_path):
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found: {config_path}. Try putting the full path or the ")
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
        return config
    

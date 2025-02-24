import os
import json
from pathlib import Path

class ConfigManager:
    def __init__(self):
        self.config_dir = Path.home() / '.scanwich'
        self.config_file = self.config_dir / 'config.json'
        self.ensure_config_dir()

    def ensure_config_dir(self):
        """Create config directory if it doesn't exist"""
        self.config_dir.mkdir(exist_ok=True)
        
    def get_api_key(self):
        """Get API key from config file or prompt user"""
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                config = json.load(f)
                return config.get('openai_api_key')
        return None

    def save_api_key(self, api_key):
        """Save API key to config file"""
        config = {'openai_api_key': api_key}
        with open(self.config_file, 'w') as f:
            json.dump(config, f)

    def setup_config(self):
        """Interactive setup for configuration"""
        if not self.get_api_key():
            print("OpenAI API key not found.")
            api_key = input("Please enter your OpenAI API key: ").strip()
            self.save_api_key(api_key)
            print(f"API key saved to {self.config_file}")
        return self.get_api_key() 
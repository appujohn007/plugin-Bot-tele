import os
import importlib
from pyrogram import Client

# Load token and API credentials from config.py
from config import API_ID, API_HASH, BOT_TOKEN

# Function to dynamically load plugins
def load_plugins(app):
    plugins_folder = 'plugins'
    for filename in os.listdir(plugins_folder):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = f"{plugins_folder}.{filename[:-3]}"
            module = importlib.import_module(module_name)
            if hasattr(module, 'register'):
                module.register(app)

def main():
    app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

    # Load all plugins
    load_plugins(app)

    app.run()

if __name__ == '__main__':
    main()

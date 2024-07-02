from pyrogram import Client, filters

def start(client, message):
    message.reply_text('Hello! Welcome to the bot.')

def register(app: Client):
    app.add_handler(filters.command("start") & filters.private, start)

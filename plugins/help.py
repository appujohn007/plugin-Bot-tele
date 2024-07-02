from pyrogram import Client, filters

def help_command(client, message):
    message.reply_text('This is the help section.')

def register(app: Client):
    app.add_handler(filters.command("help") & filters.private, help_command)

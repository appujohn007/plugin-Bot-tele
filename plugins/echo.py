from pyrogram import Client, filters

def echo(client, message):
    message.reply_text(message.text)

def register(app: Client):
    app.add_handler(filters.text & filters.private & ~filters.command, echo)

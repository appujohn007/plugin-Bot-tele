from pyrogram import Client, filters

@Client.on_message(filters.text & filters.private)
def echo(client, message):
    message.reply_text(message.text)

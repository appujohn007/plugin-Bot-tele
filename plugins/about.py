from pyrogram import Client, filters

@Client.on_message(filters.command("about") & filters.private)
def help_command(client, message):
    message.reply_text('Hello this is the about section.')

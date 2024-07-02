from pyrogram import Client, filters

@Client.on_message(filters.command("help") & filters.private)
def help_command(client, message):
    message.reply_text('This is the help section.')

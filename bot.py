from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

def main():
    app = Client(
        "my_bot",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN,
        plugins=dict(root="plugins")
    )

    app.run()

if __name__ == '__main__':
    main()


import pyrogram
from pyrogram import Client, filters
from pyrogram.types import User, Message
import os
import requests

from dotenv import load_dotenv

load_dotenv()

app = Client(
    "pastekanbot",
    bot_token=os.environ["BOT_TOKEN"],
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
)


@app.on_message(filters.command(["start"]))
async def start(bot, update):
 txt = await update.reply_text("Halo ! saya adalah bot dari pastekan.cf")



BASE = "https://pastekan.cf"


@app.on_message(filters.command(["paste"]))
def pastekan(client, message):
    message.reply_text("`pasting...`")
    text = message.reply_to_message.text if message.reply_to_message else message.text[7:]
    reply = message.reply_to_message

    if reply.text is None:
        return

    result = requests.post(
        "{}/documents".format(BASE),
        data=reply.text.encode("UTF-8")
    ).json()

    message.reply(
        "{}/{}".format(BASE, result["key"]),
        reply_to_message_id=reply.message_id
    )
    
    
print("bot aktif !")

app.run()

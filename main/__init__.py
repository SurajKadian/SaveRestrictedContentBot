#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID =25771027
API_HASH ="2f5282a8905193510998342310d7853d"
BOT_TOKEN ="6316167652:AAFCoXZEeQ14iE9EP9is8X1Kwg4LNmQk3ik"
SESSION = "BQCtuxAYlCVndU4BCbTb3nQCjX9vKpxr0ro8PR8PZppMhobEZ7puL04wDkUblPjUOmuDweRxgEFo_l9JWCV-077Iv98wkgW5JQTktC7sBJLlGN2CAjcvZCZaPA0Lo_JhfZoHmavvhUHVP0HXchRNrOi2cI39e0Wi8CDR_0uAFHy3nBfrzXmOImJqJWs3-LYjbXpyFqcU-xBUaEG2R6kkCJ3XsIoeu31jRS6LpIXZhtOH-NjJQFm5SZsYjjKEhAik81eo5vhLE73SeWDpkh-p9zG6-dpuBBCTEUnlkMVKewy63nV0r924C4cfBs8ioQ7A3DxcK0vhC9fVse9fl5xXhGCbAAAAAXkM8fcA"
FORCESUB ="k00ntentsavebot"
AUTH =6325858807

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)

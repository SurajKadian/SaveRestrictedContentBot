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
SESSION = "BQCc9no7ZOSlooU86L0YnnrNXRxG6wODwnHplCIeOxrWrTHaVvYvNoCzlfLJ-wILI8YbL_nhHHEYZy6Jpot_BfeRdCdqhEosKrUXCViLGSzhbK44XHNsM4S8xv12iTN-K-TNjwOZNrmJS_c_b5bWWaLF6YXulWM60BXpYKnAKTJiRF8GQrr1STkPV_da9z0GyTHItjORa1jz5e21bCIKN55cJo1TwnOIf8Q-suFeapffp3oG1St0s-hoICDU_8tBCBdx5OkuMc0rrAQ_648X_MMpUwPW48y5V6d44yBjITDficEgGGTM3Annj8TUsX_SDjfwhdWkszRxg6V4bTp87goBAAAAAXkM8fcA"
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

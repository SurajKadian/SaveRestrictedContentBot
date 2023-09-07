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
SESSION ="BQCKUMzkIC5bT3porcQGNB95m_SBi7_jtDseJDuym6kis0RGrPIzkzA7QIseEDpWyo0PRSFskbUcFCNZMjFU5UQT26H8thInETIfmUFY4PbVN-wCVd03ic_4aE78Ef3sO6d67rPPh7yyIg-S0aRXZ2CQNFPw8TnQfXdcKTqFcQ6lIm58i37N78AcC_UG_QCKQnkHZQKBsmA2hkgWcAcLAU9nHGBdry8n6-TWQM6VLsPzqzkctJ4ywn4znBP6s-useD90jri9nQAAw9TnJu6ZlmtfGlhbIZwOTgQzcvzrCh_nwmeQ4oPd4T1j9wrjhgWQlhWg9GXdNs8sYJAf4k1Kz27mAAAAAXkM8fcA"
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

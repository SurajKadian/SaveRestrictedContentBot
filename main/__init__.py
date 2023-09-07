#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID =28601068
API_HASH ="ce0fd56086c6ac8678dc4e888280385d"
BOT_TOKEN ="6337320640:AAF6SJLxwfiMvA9EXJq_rA4y7JcEOnCDnpU"
SESSION = "BQAW_bOMe_nAH2HqkzqrCADwqAUY7jq-0OIVEopJEpfZ57c2GZslvUGi5Im5ZsJRIHY4BmzFsZ83K5Bnxa5xr11Jf9hGDfz_vIcmFflPf-kZSnQK1QPMHtWVnlpfRDzA5P3L2vHvmHhYHUAmF3WqiTGIf3Qu-6T3DWoNjkXBKyw0ykCGtwvWe0oNWbvPZuSpSx-bZQaUkt-9gSHNbJAed4yLRkdrTecpfJvlprQ90kQyDmBW8EMguCgxtUC7d5i98On6aiUBrm1yFZ1dnjyVp9enlDzSqelGdhfRJcWPMMhFluaQLNEnN2IDF6wBJbcKqseFkdz7Sc60dDi30jwC6E5OAAAAAY5K3JkA"
FORCESUB ="k00ntent"
AUTH =6682238105

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

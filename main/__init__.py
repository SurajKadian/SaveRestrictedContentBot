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
SESSION = "BQAcuxGOB1AQ1wgU8eLAR9XeB36893f0RAEK1zozUAAnm-FOG0KCLt25clg2Q2V966tQsVwD96Amd600MQxWQDNYzk7MXYFp4An7UBhv6uyA43iSLRoiFxkT_0jnbCGV8b3GYv20lQLV0LT14kWyexxuUVzPCthE3BS9ZOaLsMEtDFYz4DFqhtfwTEyYcy8SAbZGxS7oPibK89ue0OVLcYESR2M6TGhx5anSCS6EjfPXQLkIJfgsO8dfG8TNwjb1PFBp6tB7ebRVxUGKShFmcOA4CVPv2Dws4XfYfUXa94MQlHAwGaXxNUkpFUxqSJKSRMABuEis9xDnRAClFkLZYUMsAAAAAXkM8fcA"
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

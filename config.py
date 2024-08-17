# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper




import os
import logging
from logging.handlers import RotatingFileHandler




TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7157102996:AAHxnKbFJANqdn3KaT1RwvcFWpfpxHgffr0")
APP_ID = int(os.environ.get("APP_ID", "20937822"))
API_HASH = os.environ.get("API_HASH", "68d3b463d3c53536782545f790aa5147")


OWNER = os.environ.get("OWNER", "@anmol0700") #Owner username
OWNER_ID = int(os.environ.get("OWNER_ID", "1663603208")) #Owner user id
DB_URL = os.environ.get("DB_URL", "mongodb+srv://anmol0700:anmol0700@cluster0.p1awesn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "miguel0700")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002189217539"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001938162468"))


SECONDS = int(os.getenv("SECONDS", "600")) # auto delete in seconds



PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))




START_MSG = os.environ.get("START_MESSAGE", "<b> ​🇭​​🇪​​🇱​​🇱​​🇴​ {first} 🥵\n\nɪ'ᴍ ʏᴏᴜʀ ᴍᴏᴍᴍʏ 😋💦 \n\nʏᴏᴜ ᴄᴀɴ ᴜɴᴅʀᴇꜱꜱ ᴍᴇ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ꜰɪʟᴇꜱ ꜱʜᴀʀᴇᴅ ʙʏ ᴍʏ ᴏᴡɴᴇʀ 😈\n\nᴘᴏᴡᴇʀᴇᴅ ʙʏ <a href='https://t.me/anmol0700'>ᴍɪɢᴜᴇʟ ᴏ'ʜᴀʀᴀ! 🖤</a></b>")

try:
    ADMINS=[7085541484]
    for x in (os.environ.get("ADMINS", "1844080002 1663603208").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")


FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>Hello {first}\n\n<b>You need to join in my Channel/Group to use me</b>")

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>Join @FindMyMommy 🥵</b>")

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b>ᴀʜʜ ꜱᴡᴇᴇᴛɪᴇ ! 😋\n\n❌ ᴅᴏɴ'ᴛ ꜱᴇɴᴅ ᴍᴇ ᴍᴇꜱꜱᴀɢᴇꜱ ᴅɪʀᴇᴄᴛʟʏ.</b>"

ADMINS.append(OWNER_ID)
ADMINS.append(7085541484)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper

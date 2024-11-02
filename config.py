# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper




import os
import logging
from logging.handlers import RotatingFileHandler




TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7488363157:AAFIgo_pyqfdP2PohBRRc2iFv6IEt4Rbb7s")
APP_ID = int(os.environ.get("APP_ID", "28243586"))
API_HASH = os.environ.get("API_HASH", "4022d5686b9b7a7cf8891205921a0ab3")


OWNER = os.environ.get("OWNER", "@Fushiguro_x") #Owner username
OWNER_ID = int(os.environ.get("OWNER_ID", "5961139833")) #Owner user id
DB_URL = os.environ.get("DB_URL", "mongodb+srv://madarazbotz:diQL9PIYk3sRWS0x@cluster0.zfizq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "cluster0")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002392107070"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002483117711"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1001914550244"))


SECONDS = int(os.getenv("SECONDS", "600")) # auto delete in seconds



PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))




START_MSG = os.environ.get("START_MESSAGE", "<b>Hello {first}\n\nI can store private files in Animes Duo Channel and other users can access it from special link. \n\n ᴘᴏᴡᴇʀᴇᴅ ʙʏ <a href='https://t.me/VR_unreal'>ᴠʀ ᴜɴʀᴇᴀʟ✨</a></b>")

try:
    ADMINS=[6929340267]
    for x in (os.environ.get("ADMINS", "7871556756 6447084129 5961139833 6586546549").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")


FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot !"

ADMINS.append(OWNER_ID)
ADMINS.append(6929340267)

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

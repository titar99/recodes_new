import os
from dotenv import load_dotenv

load_dotenv(".env")

API_ID = int(os.getenv("API_ID", "24300557")) 
API_HASH = os.getenv("API_HASH", "8a63cf3365dc553dbeab617d03776522") 
BOT_TOKEN = os.getenv("BOT_TOKEN", "7501322705:AAGr5AawoPXuXN_cO69qfum2UzA5qKAslgU") 
OWNER_ID = int(os.getenv("OWNER_ID", "7383553662")) 
LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002367286705"))
BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002367286705 -1002315219516 -1002239800569").split()))
MAX_BOT = int(os.getenv("MAX_BOT", "50"))
RMBG_API = os.getenv("RMBG_API", "b5ZnjZ2nUUpbdEHfcrWdjWbC")
AI_GOOGLE_API = os.getenv("AI_GOOGLE_API", "AIzaSyAM4A7L0Qj3loDZDupt0X74PDne6Tx2YLA")
DEVS = list(map(int, os.getenv("DEVS", "7383553662 6568046805").split()))
MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://vinauserbot:titar99@cluster0.z9fbe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
)
DEVS = list(map(int, os.getenv("DEVS", "927338035 7383553662").split()))

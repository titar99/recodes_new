import os
from dotenv import load_dotenv

load_dotenv(".env")

API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
OWNER_ID = int(os.getenv("OWNER_ID", ""))
LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-"))
BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002191128267 -1002226432627 -1002204672639 -1002239800569 -1001876092598 -1001986858575 -1002058863067 -1002063271971 -1002204672639 -1001571197486 -1002189271113 -1002135615153 -1002180995579 ").split()))
MAX_BOT = int(os.getenv("MAX_BOT", "50"))
RMBG_API = os.getenv("RMBG_API", "")
AI_GOOGLE_API = os.getenv("AI_GOOGLE_API", "")
MONGO_URL = os.getenv(
    "MONGO_URL",
    "",
)

DEVS = list(map(int, os.getenv("DEVS", "927338035").split()))

import os



# Required Variables Config
API_ID = int(os.environ.get("API_ID", "23159366"))
API_HASH = os.environ.get("API_HASH", "4623dd30dd1303bddb729eb0862262d9")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6445313734:AAE3nqsm9CD5a31FubeUx5ZBzahXoN4RimE")
ADMIN = int(os.environ.get("ADMIN", "5222155765"))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", "WarriorUnitsBots")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001987727042"))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://testbot:testbot@cluster0.7rzwxwx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "CodeXBots")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/0c3c0a72ca2785c0cf910.jpg")

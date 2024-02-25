# yooo guiz Herox 
import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQCpNlJyU9HHmwM1Z8w_BNwbCqEWQ3AXsOHK3FcOyVPji-3kU16ujfKhx8eAumyQPA9niyDObd9m8J77l-ZBHFmFDfAK8XDZRma7BDgNzcuyshAwTgcFJhzqGSOozxMAviIJxNztmnqBY2E-YslbRMPzNgyrXbDOrRNmWBq87UaO0RKwrhhRosDy3gM86e0qx_kNXK0ftr7uNPF6U3cfLcXJPocuJw6212WGwMf6ZHB_SEjyphvFNPEXXtEyEYVOc1omUBW-8VXkd4Xu1KgagupprBKsmRWE7p-jxT60XoWdID1acuHQUXKq-dQfgJkvZMyjJg3MaMmHdAGN5DeJJJoOAAAAATNNeNQA")
BOT_TOKEN = getenv("BOT_TOKEN", "6356990312:AAGxoiDJN2PEdyiIYCahCfxKhOz35Ztxi0o")
BOT_NAME = getenv("BOT_NAME", "xgfhfbg")
API_ID = int(getenv("API_ID", "29775178"))
API_HASH = getenv("API_HASH", "5e8b05310a39cc081983fa440f5bf030")
OWNER_NAME = getenv("OWNER_NAME", "Akbar")
ALIVE_NAME = getenv("ALIVE_NAME", "hbvhhvhb")
BOT_USERNAME = getenv("BOT_USERNAME", "cgfhtedg_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "TrickyAbhi_Assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "TrickyAbhii_Op")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Techno_Trickop")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5155682516").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/44089cf299cc80bba7c74.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "70"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/SJMxADITI/HellMusic")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/596f75a52ea9bf0109644.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/92e8c83e9148c6fea5f3b.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/92e8c83e9148c6fea5f3b.png")


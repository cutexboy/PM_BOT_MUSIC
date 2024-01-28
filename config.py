import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


API_ID = int(getenv("API_ID","")) # Get this value from my.telegram.org/apps
API_HASH = getenv("API_HASH","") # Get this value from my.telegram.org/apps
BOT_TOKEN = getenv("BOT_TOKEN") # Get your token from @BotFather on Telegram.
MONGO_DB_URI = getenv("MONGO_DB_URI", None) # Get your mongo url from cloud.mongodb.com
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "15000"))
LOGGER_ID = int(getenv("LOGGER_ID", None))  # Chat id of a group for logging bot's activities/ Music Play Logs
PUBLICELOGS = int(getenv("PUBLICELOGS", None)) # Chat id of a group for Bot Added Messege/Leaved Messege U can Add Your Support Group id Aslo
GBANLOGS = int(getenv("GBANLOGS", None)) #Add Here Your Gbans Logs Channel Id 
OWNER_ID = int(getenv("OWNER_ID", None)) # Get this value from @Sophia_x_MusicBot on Telegram by /id
## Fill these variables if you're deploying on heroku.
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")# Your heroku app name
HEROKU_API_KEY = getenv("HEROKU_API_KEY") # Get it from http://dashboard.heroku.com/account
UPSTREAM_REPO = getenv("UPSTREAM_REPO","https://github.com/cutexboy/PM_BOT_MUSIC",)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)# Fill this variable if your upstream repository is private
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/The_F2F_Shayri")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+XpchEgYvR5UxYzE1")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", "False")) # Set this to "False" if you want the assistant to automatically leave chats after an interval
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170") #Leave it
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc") #Leave it
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25)) #Leave it
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000")) #Leave it
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000")) #Leave it
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
AMBOT = [
]

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
START_IMG_URL = ["https://telegra.ph/file/a4140e3cd950e98f385c4.jpg",
                ]
PING_IMG_URL = getenv("PING_IMG_URL", "https://te.legra.ph/file/b8a0c1a00db3e57522b53.jpg")
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = getenv("STATS_IMG_URL","https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg")
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))
DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )
if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )

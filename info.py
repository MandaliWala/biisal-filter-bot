import re
import os
from os import environ
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#main variables
API_ID = int(environ.get('API_ID', '25163484'))
API_HASH = environ.get('API_HASH', '145bcbc424d1c1ffe04f3e607ea55c9a')
BOT_TOKEN = environ.get('BOT_TOKEN', '')

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6302921275 5019668523').split()]
USERNAME = environ.get('USERNAME', "https://telegram.me/Spider_Man_02")
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002137528664'))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/requestxultron')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002075429339 -1002145382878 -1001934525883 -1002039117054 -1002004849968 -1002073480988 -1002087386412 -1002121649557 -1001584064219 -1001749313075 -1002038633493 -1002137528664 -1002077178570 -1002029547741 -1002077178570 -1001613574728 -1002048583251 -1001482631371 -1002019402843 -1002019646585 -1002199963727 -1002148773240 -1001972977023 -1001942558541 -1002083199283 -1001972977023 -1001942558541 -1002083199283 -1001658823824 -1001116179493 -1002137528664 -1001609906203 -1001925233125 -1002094057193 -1002020242463 -1002079712359  -1002165297790 -1002158385438 -1002026546209 -1002228043698 -1001836124367 AV1world -1002101938265 -1002218808599 -1002004346552 -1001359686523 -1002004346552 -1002177674758 -1002233567861 -1002239734551 -1002196649548 -1002004346552 -1002126324229 -1001992468069 -1002090255299 -1001416240381 -1002048469984 -1002070431155 -1001756564118 -1002454842046').split()]
DATABASE_URI = environ.get('DATABASE_URI', "")

DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002137528664'))
QR_CODE = environ.get('QR_CODE', '')
START_IMG = environ.get('START_IMG', 'https://graph.org/file/1133ec9f62c1b3aad6865.jpg')
BIN_CHANNEL = int(environ.get('BIN_CHANNEL','-1002137528664'))
DELETE_CHANNELS = int(environ.get('DELETE_CHANNELS','-1001905670346'))
URL = environ.get('URL', '')
STICKERS_IDS = ('CAACAgQAAxkBAAEK99dlfC7LDqnuwtGRkIoacot_dGC4zQACbg8AAuHqsVDaMQeY6CcRojME').split()
FILE_AUTO_DEL_TIMER = int(environ.get('FILE_AUTO_DEL_TIMER', '600'))
IS_VERIFY = is_enabled('IS_VERIFY', False)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002137528664'))
TUTORIAL = environ.get("TUTORIAL", "https://t.me/Movie_Url_link_downloader/17")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "5bb6e402dd86fb8774690a5f4a65d2a2c0c04877")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", 'shortslink.in')
SHORTENER_API2 = environ.get("SHORTENER_API2", "41a89e7a1f16e7dbec0ee52d743f3b5a38a09613")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", 'shortslink2.com')
SHORTENER_API3 = environ.get("SHORTENER_API3", "f287e7e9b1a23c34f542f77787d39607cae36a4d")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", 'shortslink3.online')
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "14400"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "14400"))

LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam", "bengali", "marathi", "gujarati", "punjabi"]
QUALITIES = ["HdRip","web-dl" ,"bluray", "hdr", "fhd" , "240p", "360p", "480p", "540p", "720p", "960p", "1080p", "1440p", "2K", "2160p", "4k", "5K", "8K"]
YEARS = [f'{i}' for i in range(2024 , 2002,-1 )]
SEASONS = [f'season {i}'for i in range (1 , 23)]
REF_PREMIUM = 30
PREMIUM_POINT = 1500
auth_channel = environ.get('AUTH_CHANNEL', '-1002393151039')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1002125406041'))
request_channel = environ.get('REQUEST_CHANNEL', '')
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None
UPI_PAY_LOGS = int(environ.get('UPI_PAY_LOGS', '-1002137528664'))
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '-1002137528664'))

AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '5000')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 300))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)
SETTINGS = {
            'spell_check': SPELL_CHECK,
            'auto_filter': AUTO_FILTER,
            'file_secure': PROTECT_CONTENT,
            'auto_delete': AUTO_DELETE,
            'template': IMDB_TEMPLATE,
            'caption': FILE_CAPTION,
            'tutorial': TUTORIAL,
            'shortner': SHORTENER_WEBSITE,
            'api': SHORTENER_API,
            'shortner_two': SHORTENER_WEBSITE2,
            'api_two': SHORTENER_API2,
            'log': LOG_VR_CHANNEL,
            'imdb': IMDB,
            'link': LINK_MODE, 
            'is_verify': IS_VERIFY, 
            'verify_time': TWO_VERIFY_GAP,
            'shortner_three': SHORTENER_WEBSITE3,
            'api_three': SHORTENER_API3,
            'third_verify_time': THREE_VERIFY_GAP
    }
DEFAULT_POST_MODE = {
    'singel_post_mode' : False,
    'all_files_post_mode' : False
}

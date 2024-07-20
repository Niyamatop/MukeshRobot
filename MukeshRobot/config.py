class Config(object):
    LOGGER = True
    API_ID = "28298365" 
    API_HASH = "9647ab7fc03a8a93f701a5528b2f206e"
    TOKEN = "7203229265:AAE28YOfCAzCg2LCs8wBvStIGJthpRIY9LQ"  
    OWNER_ID=None
    
    SUPPORT_CHAT = "" 
    START_IMG = "https://graph.org/file/9fe22ae18601451a70189.jpg"
    EVENT_LOGS = (-1002239117016)
    MONGO_DB_URI= "mongodb+srv://Dark123:Dark123@cluster0.jsapbqx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
   
    DATABASE_URL = "postgres://avnadmin:AVNS_gwvtPgMcQ7IX0qwaCG9@freedb-mayrice01.i.aivencloud.com:14358/defaultdb?sslmode=require"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        ""
    )
    TIME_API_KEY = ""

    
    BL_CHATS = [] 
    DRAGONS = []
    DEV_USERS = []  
    DEMONS = [] 
    TIGERS = []  
    WOLVES = [] 

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

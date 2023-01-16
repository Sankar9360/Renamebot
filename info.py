import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
    
    {
    "name": "WebX Renamer Bot",
    "description": "Telegram File Renamer Bot ",
    "keywords": ["Renamer Bot", "Mongo DB"],    
    "repository": "https://github.com/WebX-Renamer-Bot",
    "env": {
        "API_ID": {
            "description": "Your APP ID From my.telegram.org ",
            "value": "23990433"
        },
        "API_HASH": {
            "description": "Your API Hash From my.telegram.org ",
            "value": "e6c4b6ee1933711bc4da9d7d17e1eb20"
        },
        "FORCE_SUB": {
            "description": "Your force sub channel user name without [@] ",
            "value": "SK_MoviesOffl",
            "required": false 
        },
        "BOT_TOKEN": {
            "description": "Your Bot Token From @BotFather",
            "value": "5964494060:AAFfOEerT8lR8YqyEHJQtbFQidqkqkYUaO8"
        },
        "ADMIN": {
            "description":"Add Your User ID multiple is use space to split",
            "value": "5821871362"
        },
        "DB_URL": {
            "description": "Your Mongo DB URL Obtained From mongodb.com",
            "value": "mongodb+srv://Test:1234@cluster0.2bzsp0q.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        },
        "DB_NAME":{ 
            "description":"Your Mongo DB Database Name ",
            "value": "Cluster0",
            "required": false
        },
        "START_PIC": {
            "description": "Your Bot start cmd Pic",
            "value": "",
            "required": false
        }
    },
    "buildpacks": [
        {
            "url": "heroku/python"
        }
    ]
}

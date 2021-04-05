import os

# The prefix that will be used to parse commands.
# It doesn't have to be a single character!
COMMAND_PREFIX = "v!"

# The bot token. Keep this secret!
BOT_TOKEN = "ODI4NDc1NTk5MDMwOTc2NTEy.YGqIBw.JFPgF1oKBUMri8E_FS5gkyBkNrA"

# The now playing game. Set this to anything false-y ("", None) to disable it
NOW_PLAYING = COMMAND_PREFIX + "help"

# Base directory. Feel free to use it if you want.
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

DEV = True

ranks = {
    "Unrated": 0,
    
    "Iron 1": 50,
    "Iron 2": 150,
    "Iron 3": 250,

    "Bronze 1": 350,
    "Bronze 2": 450,
    "Bronze 3": 550,
 
    "Silver 1": 650,
    "Silver 2": 750,
    "Silver 3": 850,

    "Gold 1": 950,
    "Gold 2": 1050,
    "Gold 3": 1150,

    "Plat 1": 1250,
    "Plat 2": 1350,
    "Plat 3": 1450,

    "Diamond 1": 1550,
    "Diamond 2": 1650,
    "Diamond 3": 1750,
 
    "Immortal": 1850,
    "Radiant": 1950,

}
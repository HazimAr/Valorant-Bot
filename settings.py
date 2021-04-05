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

    "iron 1": 50,
    "iron 2": 150,
    "iron 3": 250,

    "bronze 1": 350,
    "bronze 2": 450,
    "bronze 3": 550,
 
    "silver 1": 650,
    "silver 2": 750,
    "silver 3": 850,

    "gold 1": 950,
    "gold 2": 1050,
    "gold 3": 1150,

    "plat 1": 1250,
    "plat 2": 1350,
    "plat 3": 1450,

    "diamond 1": 1550,
    "diamond 2": 1650,
    "diamond 3": 1750,
 
    "immortal": 1850,
    "radiant": 1950,

}
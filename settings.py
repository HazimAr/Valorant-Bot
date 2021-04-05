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
import os

# The prefix that will be used to parse commands.
# It doesn't have to be a single character!
COMMAND_PREFIX = "b!"

# The bot token. Keep this secret!
BOT_TOKEN = "ODA2NjM3NjM4NjY0MDYwOTI5.YBsV1w.oNgELJmB_C9-feoMsS1lLxgdj8A"
# BOT_TOKEN = "NzQ2NzgzOTQ4NTYyMTA0MzUx.X0FWvw.vmzwSaqYKl-G2opC-n4vU5QZV_E"

# The now playing game. Set this to anything false-y ("", None) to disable it
NOW_PLAYING = COMMAND_PREFIX + "help"

# Base directory. Feel free to use it if you want.
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

from time import sleep
import requests
import json
from os.path import join
from os import remove

from discord import HTTPException
from emoji import emojize
import random

import settings


# Returns a path relative to the bot directory
def get_rel_path(rel_path):
    return join(settings.BASE_DIR, rel_path)


# Returns an emoji as required to send it in a message
# You can pass the emoji name with or without colons
# If fail_silently is True, it will not raise an exception
# if the emoji is not found, it will return the input instead
def get_emoji(emoji_name, fail_silently=False):
    alias = emoji_name if emoji_name[0] == emoji_name[-1] == ":" \
        else f":{emoji_name}:"
    the_emoji = emojize(alias, use_aliases=True)

    if the_emoji == alias and not fail_silently:
        raise ValueError(f"Emoji {alias} not found!")

    return the_emoji


# A shortcut to get a channel by a certain attribute
# Uses the channel name by default
# If many matching channels are found, returns the first one
def get_channel(client, value, attribute="name"):
    channel = next((c for c in client.get_all_channels()
                    if getattr(c, attribute).lower() == value.lower()), None)
    if not channel:
        raise ValueError("No such channel")
    return channel


# Shortcut method to send a message in a channel with a certain name
# You can pass more positional arguments to send_message
# Uses get_channel, so you should be sure that the bot has access to only
# one channel with such name
async def send_in_channel(client, channel_name, *args):
    await client.send_message(get_channel(client, channel_name), *args)


# Attempts to upload a file in a certain channel
# content refers to the additional text that can be sent alongside the file
# delete_after_send can be set to True to delete the file afterwards
async def try_upload_file(client, channel, file_path, content=None,
                          delete_after_send=False, retries=3):
    used_retries = 0
    sent_msg = None

    while not sent_msg and used_retries < retries:
        try:
            sent_msg = await client.send_file(channel, file_path,
                                              content=content)
        except HTTPException:
            used_retries += 1

    if delete_after_send:
        remove(file_path)

    if not sent_msg:
        await client.send_message(channel,
                                  "Oops, something happened. Please try again.")
    return sent_msg


def randomize_teams(message):
    vc = message.author.voice.channel
    players = vc.members
    
    team_one_choose = True

    team1 = []
    team2 = []

    less_players = bool(random.getrandbits(1))

    for i in range(len(players)):
        random1 = random.choice(players)

        if less_players:
            if team_one_choose:
                team1.append(f"<@!{random1.id}>") 
                team_one_choose = False
            else:
                team2.append(f"<@!{random1.id}>")
                team_one_choose = True

        else:
            if team_one_choose:
                team2.append(f"<@!{random1.id}>")
                team_one_choose = False

            else:
                team1.append(f"<@!{random1.id}>")
                team_one_choose = True
        
        players.remove(random1)
    
    msg = f"Attacking: {team1}\n\nDefending: {team2}"

    return msg
from time import sleep
import requests
import json
from os.path import join
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os

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
    alias = emoji_name if emoji_name[0] == emoji_name[-1] == ":" else f":{emoji_name}:"
    the_emoji = emojize(alias, use_aliases=True)

    if the_emoji == alias and not fail_silently:
        raise ValueError(f"Emoji {alias} not found!")

    return the_emoji


# A shortcut to get a channel by a certain attribute
# Uses the channel name by default
# If many matching channels are found, returns the first one
def get_channel(client, value, attribute="name"):
    channel = next(
        (
            c
            for c in client.get_all_channels()
            if getattr(c, attribute).lower() == value.lower()
        ),
        None,
    )
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
async def try_upload_file(
    client, channel, file_path, content=None, delete_after_send=False, retries=3
):
    used_retries = 0
    sent_msg = None

    while not sent_msg and used_retries < retries:
        try:
            sent_msg = await client.send_file(channel, file_path, content=content)
        except HTTPException:
            used_retries += 1

    if delete_after_send:
        os.remove(file_path)

    if not sent_msg:
        await client.send_message(
            channel, "Oops, something happened. Please try again."
        )
    return sent_msg


async def move_list_to_channel(player_list, channel, client):
    voice_channel = client.get_channel(channel)
    if voice_channel.id != settings.lobby:
        for i in player_list:
            await i.move_to(voice_channel)
        return True

    return False


async def randomize_teams(message, client):
    try:
        vc = message.author.voice.channel
        players = vc.members
    except:
        msg = "You are currently not connected to a voice channel. To use this command please connect to a voice channel"
        return msg

    team_one_choose = True

    team1 = []
    team1_move = []

    team2 = []
    team2_move = []

    less_players = bool(random.getrandbits(1))

    for i in range(len(players)):
        random1 = random.choice(players)

        if less_players:
            if team_one_choose:
                team1.append(random1.mention)
                team1_move.append(random1)
                team_one_choose = False
            else:
                team2.append(random1.mention)
                team2_move.append(random1)
                team_one_choose = True

        else:
            if team_one_choose:
                team2.append(random1.mention)
                team2_move.append(random1)
                team_one_choose = False
            else:
                team1.append(random1.mention)
                team1_move.append(random1)
                team_one_choose = True

        players.remove(random1)

    msg = f"You will be moved to your respected channels\n\nAttacking: {team1}\nDefending: {team2}"

    vc = await move_list_to_channel(team1_move, settings.attacking, client)
    if not vc:
        return f"Please join <#{settings.lobby}>"
    vc = await move_list_to_channel(team2_move, settings.defending, client)
    if not vc:
        return f"Please join <#{settings.lobby}>"

    return msg


def get_user_rank(user, tag):
    if settings.DEV:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(
            executable_path="D:/Code/Discord/Valorant-Bot/chromedriver",
            chrome_options=chrome_options,
        )
    else:
        chrome_options = Options()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")

        driver = webdriver.Chrome(
            executable_path=os.environ.get("CHROMEDRIVER_PATH"),
            chrome_options=chrome_options,
        )

    web = f"https://tracker.gg/valorant/profile/riot/{user}%23{tag}/overview?playlist=competitive"
    driver.get(web)

    rank_xpath = "/html/body/div[1]/div[2]/div[2]/div/main/div[2]/div[3]/div[3]/div[4]/div[2]/div[2]/div/div[1]/div[1]/span[2]"

    # def Click(xpath):
    #     driver.find_element_by_xpath(xpath).click()

    # def SendKeys(xpath, input):
    #     driver.find_element_by_xpath(xpath).send_keys(input)

    def Wait(time, xpath):
        WebDriverWait(driver, time).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )

    try:
        Wait(5, rank_xpath)
    except:
        driver.quit()
        msg = f"{user+tag}'s account is private or has not yet played ranked\nIf you are the owner of this account and would like to make your account public please click here\nhttps://account.tracker.gg/auth/search?provider=riot&returnUrl=https://tracker.gg/auth/search/callback&state=valorant"
        return msg

    rank = driver.find_element_by_xpath(rank_xpath).text
    driver.quit()
    # msg = settings.ranks[rank]
    msg = rank

    return msg


async def end(client):
    lobby = client.get_channel(settings.lobby)
    attacking = client.get_channel(settings.attacking)
    defending = client.get_channel(settings.defending)

    for i in attacking.members:
        await i.move_to(lobby)
    for j in defending.members:
        await j.move_to(lobby)


def team_randomization(player_list, length_of_each_sub_list):
    for i in range(0, len(player_list), length_of_each_sub_list):
        yield player_list[i : i + length_of_each_sub_list]

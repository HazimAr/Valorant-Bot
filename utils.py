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
        os.remove(file_path)

    if not sent_msg:
        await client.send_message(channel,
                                  "Oops, something happened. Please try again.")
    return sent_msg


def randomize_teams(message):
    try:
        vc = message.author.voice.channel
        players = vc.members
    except:
        msg = "You are currently not connected to a voice channel. To use this command please connect to a voice channel"
        return msg
    
    team_one_choose = True

    team1 = []
    team2 = []

    less_players = bool(random.getrandbits(1))

    for i in range(len(players)):
        random1 = random.choice(players)

        if less_players:
            if team_one_choose:
                team1.append(random1.id.mention)
                team_one_choose = False
            else:
                team2.append(random1.id.mention)
                team_one_choose = True

        else:
            if team_one_choose:
                team2.append(random1.id.mention)
                team_one_choose = False

            else:
                team1.append(random1.id.mention)
                team_one_choose = True
        
        players.remove(random1)
    
    msg = f"You will be moved to your respected channels in 5 seconds\n\nAttacking: {team1}\nDefending: {team2}"

    return msg


def get_user_rank(user, tag):  
    if settings.DEV:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path="D:/Code/Discord/ValorantBot/chromedriver", chrome_options=chrome_options)
    else:
        chrome_options = Options()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")

        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

    web = f"https://tracker.gg/valorant/profile/riot/{user}%23{tag}/overview?playlist=competitive"
    driver.get(web)

    rank_xpath = "/html/body/div[1]/div[2]/div[2]/div/main/div[2]/div[3]/div[3]/div[4]/div[2]/div[2]/div/div[1]/div[1]/span[2]"

    # def Click(xpath):
    #     driver.find_element_by_xpath(xpath).click()

    # def SendKeys(xpath, input):
    #     driver.find_element_by_xpath(xpath).send_keys(input)

    def Wait(time, xpath):
        WebDriverWait(driver, time).until(EC.presence_of_element_located((By.XPATH, xpath)))
    try:
        Wait(5, rank_xpath)
    except:
        driver.quit()
        msg = f"{user+tag}'s account is private\nIf you are the owner of this account and would like to make your account public please click here\nhttps://account.tracker.gg/auth/search?provider=riot&returnUrl=https://tracker.gg/auth/search/callback&state=valorant"
        return msg
        
    rank = driver.find_element_by_xpath(rank_xpath).text
    driver.quit()
    msg = settings.ranks[rank]

    return msg
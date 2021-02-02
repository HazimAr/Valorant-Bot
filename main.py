import discord

import requests
import json

TOKEN = "ODA2MjU0OTQxNTk2NjgwMjQy.YBmxbQ.Jmy7DOgPw7CB_qMW-RV6uSsEfrY"

client = discord.Client()

prefix = '.'

sad_words = ["sad", "depressed", "unhappy", "angry", "bad", "trash"]

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):

    msg = message.content
     
    if message.author == client.user:
        return

    if msg.startswith(f"{prefix}inspire"):
        await message.channel.send(get_quote())
    
    elif any(word in msg for word in sad_words):
        await message.channel.send(get_quote())
    
    elif msg.lower() == 'pog':
        await message.channel.send("I guess you are my little pogchamp... Come here")

client.run(TOKEN)

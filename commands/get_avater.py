from commands.base_command import BaseCommand
from utils import get_emoji
import asyncio
import discord

class Av(BaseCommand):

    def __init__(self):
        description = "Returns the link to <user>'s avater."
        params = ['user']
        super().__init__(description, params)

    async def handle(self, params, message, client):
        try:
            user = client.get_user(
                int(params[0].split("<@!&",)[1].split(">")[0]))
        except:
            user = client.get_user(int(params[0]))
        print(user)
        print(params[0])
        link = user.avatar_url_as(format="png", static_format="png")
        print(link)
        msg = f"{user}'s link to their avater is {link}"
        await message.channel.send(msg)

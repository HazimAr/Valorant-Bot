from commands.base_command import BaseCommand
from utils import get_emoji
from utils import fetch

import asyncio
import discord

# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command


class Quote(BaseCommand):

    def __init__(self):
        description = "Generates a quote based on <type>, (today) and (random) are valid parameters"
        params = ['type']
        super().__init__(description, params)

    async def handle(self, params, message, client):
        api_url = f'https://zenquotes.io/api/{params[0]}'
        smile = get_emoji(':smile:')
        try:
            response = fetch(api_url)

            quote = response[0]['q']
            author = response[0]['a']

            msg = f'{quote} -{author} {smile}'
            await message.channel.send(msg)
        except:
            await message.channel.send("Please provide a valid parameter <type>, today and random are valid parameters.")

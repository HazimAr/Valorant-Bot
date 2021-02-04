from commands.base_command import BaseCommand
from utils import get_emoji

import asyncio
import discord


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class Nik(BaseCommand):

    def __init__(self):
        description = "Niko is <insult>"
        params = ['insult']
        super().__init__(description, params)

    async def handle(self, params, message, client):
        niko = '<@462102455132356608>'
        insult = params[0]
        rainbow = get_emoji(':rainbow:')
        msg = f'{niko} is {insult} also he is {rainbow}'
        await message.channel.send(msg)
        await message.channel.send(file=discord.File('.\assets\doodoo_code.png'))

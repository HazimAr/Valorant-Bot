from commands.base_command import BaseCommand
from utils import get_emoji

import asyncio
import discord


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class Banana(BaseCommand):
    def __init__(self):
        description = "Sends a banana emoji"
        params = []
        super().__init__(description, params)

    async def handle(self, params, message, client):
        msg = get_emoji(":banana:")
        await message.channel.send(msg)

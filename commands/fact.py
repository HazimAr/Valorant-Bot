from commands.base_command import BaseCommand
from utils import get_emoji
from utils import fact_of_the_day

import asyncio
import discord


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class Fact(BaseCommand):

    def __init__(self):
        description = "Generates a fact based on <type> either (today) or (random) are valid parameters"
        params = ['type']
        super().__init__(description, params)

    async def handle(self, params, message, client):
        api_url = f'https://uselessfacts.jsph.pl/{params[0]}.json'
        smile = get_emoji(':smile:')
        try:
            fact = fact_of_the_day(api_url)
            msg = f'Fact: {fact} {smile}'
            await message.channel.send(msg)
        except:
            await message.channel.send("Please provide a valid parameter <type>, today and random are valid parameters.")


        




from commands.base_command import BaseCommand
from utils import get_emoji


import asyncio
import discord


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class DeathDay(BaseCommand):

    def __init__(self):
        description = "Shows you the day you die and how much time you have left"
        params = ['age']
        super().__init__(description, params)

    async def handle(self, params, message, client):

        try:
            age = float(params[0])
        except ValueError:
            await message.channel.send("Please, provide valid numbers")
            return
        age_expectancy = 78.54
        if age <= 0:
            msg = 'your not born dummy'
        elif age > 1000:
            msg = 'why you trying to break me dummy'
        elif age >= age_expectancy:
            msg = 'you just beat death congrats'
        else:
            death_day = age_expectancy - age
            msg = f'You will live for {round(death_day, 2)} more years, {death_day * 12} more months, {round(death_day * 52.1429, 2)} more weeks, {round(death_day * 365,2)} more days, {round(death_day * 365 * 24,2)} more hours, {round(death_day * 365 * 24 * 60,2)}, more minutes, and {round(death_day * 365 * 24 * 60 * 60,2)} more seconds to live. {get_emoji(":skull:")}'
        await message.channel.send(msg)

from commands.base_command import BaseCommand
from utils import get_emoji
from random import randint


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class Receipt(BaseCommand):

    def __init__(self):
        description = "Provides a reciept of all purchases made by that user"
        params = ['user']
        super().__init__(description, params)

    async def handle(self, params, message, client):
        msg = discord.embed(title='Thank you for purchasing from BlockTrap')
        msg = get_emoji(":game_die:") + f" You rolled your mom!"
        await message.author.send(embed=msg)

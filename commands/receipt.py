from commands.base_command import BaseCommand

import discord


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
        user = params[0]

        msg = discord.embed(title=f'Thank you {user} for purchasing from BlockTrap')
        await message.author.send(embed=msg)
from commands.base_command import BaseCommand
import random

class Bracket(BaseCommand):

    def __init__(self):
        description = "Makes a bracket as even as possible based off of a list"
        params = None
        super().__init__(description, params)

    async def handle(self, params, message, client):
                
        map = random.choice(["Ascent‎", "Bind", "Haven", "Split", "Icebox"])
        
        msg = f"Map: {map}"

        await message.channel.send(msg)

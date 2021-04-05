from commands.base_command import BaseCommand
import random

class Map(BaseCommand):

    def __init__(self):
        description = "Picks a random valorant map"
        params = None
        super().__init__(description, params)

    async def handle(self, params, message, client):
                
        map = random.choice(["Ascent‎", "Bind", "Haven", "Split", "Icebox"])
        
        msg = f"Map: {map}"

        await message.channel.send(msg)

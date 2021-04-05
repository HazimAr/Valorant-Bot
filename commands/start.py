from commands.base_command import BaseCommand
import random
import utils

class Start(BaseCommand):

    def __init__(self):
        description = "This will randomize teams and map for the vc that you are in"
        params = None
        super().__init__(description, params)

    async def handle(self, params, message, client):

        team_msg = utils.randomize_teams(message)
        
        map = random.choice(["Ascent‎", "Bind", "Haven", "Split", "Icebox"])

        msg = f"{team_msg}\n\nMap: {map}"

        await message.channel.send(msg)

from commands.base_command import BaseCommand
import random
import utils

class Teams(BaseCommand):

    def __init__(self):
        description = "This will randomize teams for the vc that you are in"
        params = None
        super().__init__(description, params)

    async def handle(self, params, message, client):

        team_msg = await utils.randomize_teams(message, client)

        await message.channel.send(team_msg)

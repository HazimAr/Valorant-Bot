from commands.base_command import BaseCommand
import random
from settings import ranks
import utils

class Check(BaseCommand):

    def __init__(self):
        description = "Checks valorant stats"
        params = ["user"]
        super().__init__(description, params)

    async def handle(self, params, message, client):
        try:
            user = params[0].split("#")[0]; tag = params[0].split("#")[1]
        except:
            msg = "Please send the user in this format **username**#**tag**"
            await message.channel.send(msg)
            return
        msg = "Please allow up to 5 seconds for us to look up the user"
        await message.channel.send(msg)

        try:
            msg = utils.get_user_rank(message, user, tag)
        except:
            msg = "An error occurred"
        await message.channel.send(msg)

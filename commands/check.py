from commands.base_command import BaseCommand
import random
from settings import ranks
import utils

class Check(BaseCommand):

    def __init__(self):
        description = "Checks valorant stats"
        params = None
        super().__init__(description, params)

    async def handle(self, params, message, client):
        channel = message.channel
        def check(m):
            return m.author.id == message.author.id and m.channel == channel

        msg = f"Please enter the valorant username you are trying to search\nExample: HazAr#1639"
        await message.channel.send(msg)

        user = await client.wait_for("message", check=check, timeout=600.0).content
        try:
            user = user.split("#")[0]; tag = user.split("#")[1]
        except:
            msg = "Please send the user in this format **username**#**tag**"
            await message.channel.send(msg)
            return
        msg = "Please allow up to 5 seconds for us to look up the user"
        await message.channel.send(msg)

        try:
            msg = utils.get_user_rank(user, tag)
        except:
            msg = "An error occurred"
        await message.channel.send(msg)

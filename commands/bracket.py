from commands.base_command import BaseCommand
import random

import utils

class Bracket(BaseCommand):

    def __init__(self):
        description = "Makes a bracket as even as possible based off of a list"
        params = None
        super().__init__(description, params)

    async def handle(self, params, message, client):
        msg = ""
        users = ["Sakuraツ#juice", "Sakuraツ#juice", "Sakuraツ#juice", "Sakuraツ#juice", "Sakuraツ#juice"]

        for i in users:
            user = i.split("#")[0]; tag = i.split("#")[1]
            rank = utils.get_user_rank(user, tag)
            if type(rank) == int:
                msg += f"{rank}, "


        await message.channel.send(msg)

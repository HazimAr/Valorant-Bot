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
        user = ["Sakuraツ#juice", "Sakuraツ#juice", "Sakuraツ#juice", "Sakuraツ#juice", "Sakuraツ#juice"]

        for user in user:
            rank = utils.get_user_rank(user)
            if type(rank) == int:
                msg += f"{rank}, "
        

        await message.channel.send(msg)

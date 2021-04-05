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
        users = ["Sakuraツ#juice", "SyfeFPS#8099", "SoulPsych0#uwu", "tunaflip#uwu", "Misaki#levi"]
        users_rank = []
        users_and_rank = {}
        for i in users:
            await message.channel.send(f"Checking {i}")
            user = i.split("#")[0]; tag = i.split("#")[1]
            rank = utils.get_user_rank(user, tag)
            if type(rank) == int:
                msg += f"{rank}, "
                users_rank.append(rank)
            else:
                msg += "None, "
                users_rank.append(None)

        total_mmr = 0
        for i in users_rank:
            if type(i) == int:
                total_mmr += i
        average_user_mmr = total_mmr / len(users)
        msg += f"The average mmr is: {average_user_mmr}"

        for key in users:
            for value in users_rank:
                users_and_rank[key] = value
                users_rank.remove(value)
                break
        msg += str(users_and_rank)

        
        await message.channel.send(msg)
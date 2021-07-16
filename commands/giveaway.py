from commands.base_command import BaseCommand
import random
import utils
from math import floor


class Giveaway(BaseCommand):
    def __init__(self):
        description = (
            "Random Winner from Reactions"
        )
        params = None
        super().__init__(description, params)

    async def handle(self, params, message, client):
        with open("giveaway.txt", "r") as file:
            player_list = []
            for i in file:
                if i:
                    i = i.split("\n")[0]
                    player_list.append(i)

        random.shuffle(player_list)
        random_winner = random.choice(player_list)

        await message.channel.send(f"<@{random_winner}>")

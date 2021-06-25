from commands.base_command import BaseCommand
import random
import utils
from math import floor


class Random(BaseCommand):
    def __init__(self):
        description = (
            "This will randomize teams that are currently signed-up for the tournament"
        )
        params = ["team_size"]
        super().__init__(description, params)

    async def handle(self, params, message, client):
        try:
            team_size = int(params[0])
        except:
            await message.send("Please send a valid team size")

        with open("players.txt", "r") as file:
            player_list = []
            for i in file:
                if i:
                    i = i.split("\n")[0]
                    player_list.append(i)

        random.shuffle(player_list)
        random_teams = list(utils.team_randomization(player_list, team_size))

        for i in random_teams:
            for j in i:
                k = await client.fetch_user(j)
                random_teams[random_teams.index(i)][i.index(j)] = k.name
        await message.channel.send(random_teams)

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
        users = ["Sakuraツ#juice", "SyfeFPS#8099", "SoulPsych0#uwu", "tunaflip#uwu", "Misaki#levi", "TayTayy#4828", "swage#0424","milkyway#MILF"]
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
        msg += f"\nThe average mmr is: {average_user_mmr}\n"

        for key in users:
            for value in users_rank:
                users_and_rank[key] = value
                users_rank.remove(value)
                break

        users_and_rank = dict(filter(lambda elem: not(elem[1] == None), users_and_rank.items()))
        msg += str(users_and_rank)

        bracket = []
        temp_key = ""

        for i in range(len(users_and_rank.keys()) // 2):
            users_original = list(users_and_rank.keys())
            users = list(users_and_rank.keys())
            player_one_key = users[i]
            users.remove(player_one_key)

            temp_key = users[i + 1]
            
            for j in range(len(users) // 2):
                if (average_user_mmr - users_and_rank[users_original[j]]) < (average_user_mmr - users_and_rank[users_original[temp_key]]):
                    temp_key = j
                    users.remove(temp_key)
                    
            bracket.append([[player_one_key,users_and_rank[player_one_key]],[temp_key,users_and_rank[temp_key]]])
               
        await message.channel.send(msg)
        await message.channel.send(bracket)
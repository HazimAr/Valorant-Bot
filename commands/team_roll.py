from commands.base_command import BaseCommand
import random

class TeamRoll(BaseCommand):

    def __init__(self):
        description = "Will choose a random valorant agent for everyone in the vc"
        params = None
        super().__init__(description, params)

    async def handle(self, params, message, client):        
        vc = message.author.voice.channel
        try:
            players = vc.members
        except:
            msg = "You are currently not connected to a voice channel. To use this command please connect to a voice channel"
            await message.channel.send(msg)
            return
        
        msg = ""

        agents = ["Astra", "Breach", "Brimstone", "Cypher", "Jett", "Killjoy", "Omen", "Phoenix", "Raze", "Reyna", "Sage", "Skye", "Sova", "Viper", "Yoru"]

        for i in range(len(players)):
            agent = random.choice(agents)
            agents.remove(agent)
            player = f"{players[i].name}: {agent}\n"
            msg += player

        await message.channel.send(msg)

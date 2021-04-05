from commands.base_command import BaseCommand
import random

class Roll(BaseCommand):

    def __init__(self):
        description = "Will choose a random valorant agent"
        params = None
        super().__init__(description, params)

    async def handle(self, params, message, client):
                
        agent = random.choice(["Astra", "Breach", "Brimstone", "Cypher", "Jett", "Killjoy", "Omen", "Phoenix", "Raze", "Reyna", "Sage", "Skye", "Sova", "Viper", "Yoru"])
        
        msg = f"{message.author.mention}\nAgent: {agent}"

        await message.channel.send(msg)

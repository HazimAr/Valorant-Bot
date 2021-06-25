from commands.base_command import BaseCommand
import random
import settings


class Roll(BaseCommand):
    def __init__(self):
        description = "Will choose a random valorant agent"
        params = None
        super().__init__(description, params)

    async def handle(self, params, message, client):

        agent = random.choice(
           settings.agents
        )

        msg = f"{message.author.mention}\nAgent: {agent}"

        await message.channel.send(msg)

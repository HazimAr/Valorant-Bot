from commands.base_command import BaseCommand
import random
import settings

class Strat(BaseCommand):

    def __init__(self):
        description = "Will choose a random strategie that the whole team will follow"
        params = ["role"]
        super().__init__(description, params)

    async def handle(self, params, message, client):
     
        if params[0].lower().startswith('a'):
            strat = random.choice(settings.starts_a)
        elif params[0].lower().startswith('d'):
            strat = random.choice(settings.starts_d)
        else:
            await message.channel.send(f"Please enter a valid role for your team, Example: `{settings.COMMAND_PREFIX}strat attacking`")
        
        msg = f"{strat[0]}\n{strat[1]}"

        await message.channel.send(msg)

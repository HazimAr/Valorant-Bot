from commands.base_command import BaseCommand
import utils

class End(BaseCommand):

    def __init__(self):
        description = "Moves everyone from attacking and defending to lobby"
        params = None
        super().__init__(description, params)

    async def handle(self, params, message, client):
        await utils.end(client)


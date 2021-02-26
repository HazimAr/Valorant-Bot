from commands.base_command import BaseCommand

import asyncio
import discord

import random

class Somebody(BaseCommand):

    def __init__(self):
        description = "This will @ a random person in the server"
        params = []
        super().__init__(description, params)

    async def handle(self, params, message, client):
        member_list = client.get_all_members()
        random_member = random.choice(list(member_list))
        random_member_id = f'<@{random_member.id}>'

        msg = f"{random_member_id} has been chosen by the gods to be annoyed"
        await message.channel.send(msg)

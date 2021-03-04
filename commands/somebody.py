from commands.base_command import BaseCommand

import asyncio
import discord

import random

from time import sleep

class Somebody(BaseCommand):

    def __init__(self):
        description = "This will @ a random person in the server"
        params = []
        super().__init__(description, params)

    async def handle(self, params, message, client):
        member_list = list(message.guild.members)
        random_member = random.choice(member_list)
        random_member_id = f'<@{random_member.id}>'
        for i in range(len(member_list)):
            member = member_list[i]
            msg = f'<@{member.id}>'
            print(msg)
            sleep(0.5)
            await message.channel.send(msg)

        msg = f"{random_member_id} has been chosen by the gods to be annoyed"
        await message.channel.send(msg)

import sys

import settings
import discord
import message_handler

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from events.base_event import BaseEvent
from events import *
from multiprocessing import Process
import random

# Set to remember if the bot is already running, since on_ready may be called
# more than once on reconnects
this = sys.modules[__name__]
this.running = False

# Scheduler that will be used to manage events
sched = AsyncIOScheduler()

###############################################################################


def main():
    # Initialize the client
    print("Starting up...")
    intents = discord.Intents.default()
    intents.members = True
    client = discord.Client(intents=intents)

    # Define event handlers for the client
    # on_ready may be called multiple times in the event of a reconnect,
    # hence the running flag
    @client.event
    async def on_ready():
        if this.running:
            return
        this.running = True

        # Set the playing status
        if settings.NOW_PLAYING:
            print("Setting NP game", flush=True)
            await client.change_presence(
                activity=discord.Game(name=settings.NOW_PLAYING)
            )
        print("Logged in!", flush=True)

        # Load all events
        print("Loading events...", flush=True)
        n_ev = 0
        for ev in BaseEvent.__subclasses__():
            event = ev()
            sched.add_job(
                event.run, "interval", (client,), minutes=event.interval_minutes
            )
            n_ev += 1
        sched.start()
        print(f"{n_ev} events loaded", flush=True)

    # The message handler for both new message and edits
    async def common_handle_message(message):
        if message.author.bot:
            return
        text = message.content.lower()

        if text.startswith(settings.COMMAND_PREFIX) and text != settings.COMMAND_PREFIX:

            cmd_split = text[len(settings.COMMAND_PREFIX) :].split()
            try:
                await message_handler.handle_command(
                    cmd_split[0].lower(), cmd_split[1:], message, client
                )
            except:
                print("Error while handling message", flush=True)
                raise

    @client.event
    async def on_message(message):
        await common_handle_message(message)

    @client.event
    async def on_message_edit(before, after):
        await common_handle_message(after)

    @client.event
    async def on_raw_reaction_add(payload):
        if payload.message_id == settings.tourney_msg:
            with open("players.txt", "a") as file:
                file.write(f"{payload.member.id}\n")
            await payload.member.send("Thanks for siging up to the tournament")
        elif payload.message_id == settings.giveaway_msg:
            with open("giveaway.txt", "a") as file:
                file.write(f"{payload.member.id}\n")
            await payload.member.send("Thanks for siging up to the giveaway")

    @client.event
    async def on_raw_reaction_remove(payload):
        if payload.message_id == settings.tourney_msg:
            list_of_players = []
            with open("players.txt", "r") as file:
                for i in file:
                    i = i.split("\n")[0]
                    if i != str(payload.user_id):
                        list_of_players.append(f"{i}\n")
            with open("players.txt", "w") as file:
                file.write("")
            with open("players.txt", "a") as file:
                for i in set(list_of_players):
                    file.write(i)

            user = await client.fetch_user(payload.user_id)
            await user.send("You successfully left the tournament. Sorry to see you go")
        elif payload.message_id == settings.giveaway_msg:
            list_of_players = []
            with open("giveaway.txt", "r") as file:
                for i in file:
                    i = i.split("\n")[0]
                    if i != str(payload.user_id):
                        list_of_players.append(f"{i}\n")
            with open("giveaway.txt", "w") as file:
                file.write("")
            with open("giveaway.txt", "a") as file:
                for i in set(list_of_players):
                    file.write(i)

            user = await client.fetch_user(payload.user_id)
            await user.send("You successfully left the giveaway. Sorry to see you go")

    # Finally, set the bot running
    client.run(settings.BOT_TOKEN)


###############################################################################

if __name__ == "__main__":
    main()

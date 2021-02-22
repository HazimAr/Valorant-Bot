from events.base_event import BaseEvent
from utils import fact_of_the_day, get_channel, get_emoji

# Your friendly example event
# You can name this class as you like, but make sure to set BaseEvent
# as the parent class
class FactEveryday(BaseEvent):

    def __init__(self):
        interval_minutes = 24*60  # Set the interval for this event
        super().__init__(interval_minutes)

    # Override the run() method
    # It will be called once every {interval_minutes} minutes
    async def run(self, client):
        channel = get_channel(client, "fact-of-the-day")

        api_url = f'https://uselessfacts.jsph.pl/today.json'
        smile = get_emoji(':smile:')

        fact = fact_of_the_day(api_url)
        msg = f'Fact: {fact} {smile}'
        await channel.send(msg)

        

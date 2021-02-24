from events.base_event import BaseEvent
from utils import fact_of_the_day, get_channel, get_emoji
from datetime import datetime

# Your friendly example event
# You can name this class as you like, but make sure to set BaseEvent
# as the parent class
class FactEveryday(BaseEvent):
    

    def __init__(self):
        interval_minutes = 60  # Set the interval for this event
        super().__init__(interval_minutes)

    # Override the run() method
    # It will be called once every {interval_minutes} minutes
    async def run(self, client):
        now = datetime.now()
        print(now)
        if now.hour == 17:
            channel = get_channel(client, "fact-of-the-day")

            api_url = f'https://uselessfacts.jsph.pl/today.json'
            smile = get_emoji(':smile:')

            fact = fact_of_the_day(api_url)
            msg = f'Fact: {fact} {smile}'
            await channel.send(msg)
        

        

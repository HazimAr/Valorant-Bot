from events.base_event import BaseEvent
from utils import fetch, get_channel, get_emoji
from datetime import datetime

# Your friendly example event
# You can name this class as you like, but make sure to set BaseEvent
# as the parent class
class QuoteEveryday(BaseEvent):
    

    def __init__(self):
        interval_minutes = 60  # Set the interval for this event
        super().__init__(interval_minutes)

    # Override the run() method
    # It will be called once every {interval_minutes} minutes
    async def run(self, client):
        now = datetime.now()
        print(now)
        if now.hour == 13:
            channel = get_channel(client, "quote-of-the-day")

            api_url = f'https://zenquotes.io/api/today'
            smile = get_emoji(':smile:')

            response = fetch(api_url)

            quote = response[0]['q']
            author = response[0]['a']

            msg = f'{quote} -{author} {smile}'
            await channel.send(msg)
    

        

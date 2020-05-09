from telethon import TelegramClient, events

api_id = "1347918"
api_hash = "5681581438678d9390cd4f67ee764f82"
bot_token = "852053528:AAHL_ryUUJ1JOhenzmI0WDiayAnxxqGFmyU"
# with TelegramClient("shotss", api_id, api_hash) as client:
    # client.loop.run_until_complete(client.send_message('me', "hello myself"))


client = TelegramClient('testcaseo', api_id, api_hash)
# .start(bot_token=bot_token)

from telethon import errors
import logging
from parser import pasig

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

channel1 = "https://t.me/testcasechannel2"
channel2 = 'https://t.me/testcasechannel'
@client.on(
    events.NewMessage(
        chats= channel1, 
        pattern=r"^(BUY|SELL)\s([A-Z]*)\s[\(@at\s]*([0-9]*[.,][0-9]*)[\).]", 
        incoming=True
        ))
async def forwarder(event):
    text = event.message.text
    signal = pasig(text)
    output_channel = await client.send_message(channel2, signal)

client.start()
# client.add_event_handler(forwarder)
client.run_until_disconnected()

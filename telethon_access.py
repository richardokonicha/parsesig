from telethon import TelegramClient, events
import db
from telethon import errors
import logging
from parser import pasig


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
# message_pair = db.MessagePair.get_name('testcase')
message_pair = db.MessagePair.get_name('BST')

api_hash = message_pair.api_hash
api_id = message_pair.api_id
bot_token = message_pair.bot_token
try:
    channel_input = int(message_pair.channel_input)
except ValueError:
    channel_input = message_pair.channel_input
try:
    channel_output = int(message_pair.channel_output)
except ValueError:
    channel_output = message_pair.channel_output

channel_input = -1001313782946
pair_name = message_pair.pair_name
client = TelegramClient("BST_t", api_id, api_hash)


@client.on(
    events.NewMessage(
        chats= channel_input, 
        pattern=r"^(BUY|SELL)\s([A-Z]*)\s[\(@at\s]*([0-9]*[.,][0-9]*)[\).]", 
        incoming=True
        ))
async def forwarder(event):
    text = event.message.text
    signal = pasig(text)
    print(signal)
    output_channel = await client.send_message(channel_output, signal)

@client.on(events.NewMessage)
async def fresh_message(event):
    text = event.message.text
client.start()
client.run_until_disconnected()

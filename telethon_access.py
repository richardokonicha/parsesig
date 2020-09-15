from telethon import TelegramClient, events
from telethon.sessions import StringSession
# import db
from telethon import errors
import logging
from parser import pasig
import os
from dotenv import load_dotenv

from util import bot_forward
load_dotenv()

# set logging level
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

channel_input = os.getenv('CHATINPUT')
channel_input = [int(i) for i in channel_input.split(' ')]  # dont
channel_output = int(os.getenv('CHATOUTPUT')) # dont

test_input = os.getenv("TESTINPUT")
test_output = os.getenv("TESTOUTPUT")
test_input = [int(i) for i in test_input.split(' ')]  # dont

session = os.getenv("SESSION")
api_hash = os.getenv("API_HASH")
api_id = os.getenv("API_ID")

# client = TelegramClient("BST_t", api_id, api_hash)
print(session)
client = TelegramClient(StringSession(session), api_id, api_hash)

# client event handler on incoming new messages matching the regex filter from chat or channel
@client.on(
    events.NewMessage(
        chats= channel_input, 
        pattern=r"^(BUY|SELL)\s([A-Z]*)\s[\(@at\s]*([0-9]*[.,][0-9]*)[\).]", 
        incoming=True
        ))
# function takes message text that matches the regex filter and transforms using pasig transformer and sends to new channel
async def forwarder(event):
    text = event.message.text
    signal = pasig(text)
    print(signal)
    output_channel = await client.send_message(channel_output, signal)

# listens on the test channel
@client.on(
    events.NewMessage(
        chats=test_input,
        # pattern=r"^(BUY|SELL)\s([A-Z]*)\s[\(@at\s]*([0-9]*[.,][0-9]*)[\).]", 
        incoming=True,
        outgoing=True
        ))
# function takes message text that matches the regex filter and transforms using pasig transformer and sends to new channel
async def forwarderr(event):
    text = event.message.text
    bot_forward(text)
    # signal = pasig(text)
    # output_channel = await client.send_message(test_output, text)


@client.on(events.NewMessage)
async def trooper(event):
    text = event.message.text
    print(text)

client.start()
client.run_until_disconnected()

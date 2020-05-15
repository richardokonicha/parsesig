from telethon import TelegramClient, events
from telethon.sessions import StringSession
# import db
from telethon import errors
import logging
from parser import pasig
import os
from dotenv import load_dotenv
load_dotenv()

# set logging level
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

try:
    test_input = int(os.getenv("TESTINPUT"))
    channel_input = int(os.getenv('CHATINPUT'))
    test_output = int(os.getenv("TESTOUTPUT"))
    channel_output = int(os.getenv('CHATOUTPUT'))
    session = os.getenv("SESSION")
    api_hash = os.getenv("API_HASH")
    api_id = os.getenv("API_ID")
except ValueError:
    print('couldnt get env')

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
        chats= test_input, 
        pattern=r"^(BUY|SELL)\s([A-Z]*)\s[\(@at\s]*([0-9]*[.,][0-9]*)[\).]", 
        incoming=True
        ))
# function takes message text that matches the regex filter and transforms using pasig transformer and sends to new channel
async def forwarder(event):
    text = event.message.text
    signal = pasig(text)
    print(signal)
    output_channel = await client.send_message(test_output, signal)

@client.on(events.NewMessage)
async def trooper(event):
    text = event.message.text
    print(text)

client.start()
client.run_until_disconnected()

from telethon import TelegramClient, events
import db
from telethon import errors
import logging
from parser import pasig
import os
from dotenv import load_dotenv
load_dotenv()

# set logging level
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
# gets User object from db with message pair
# message_pair = db.MessagePair.get_name('testcase')
message_pair = db.MessagePair.get_name('BST')

# defines variables from message pair object
api_hash = message_pair.api_hash
api_id = message_pair.api_id
bot_token = message_pair.bot_token

# sets channels taking both string input and number input
try:
    test_input = int(os.getenv("TESTINPUT"))
    channel_input = int(os.getenv('CHATINPUT'))
except ValueError:
    # channel_input = message_pair.channel_input
    # channel_input = int(message_pair.channel_input)
    print('couldnt get env')
try:
    test_output = int(os.getenv("TESTOUTPUT"))
    channel_output = int(os.getenv('CHATOUTPUT'))
    
except ValueError:
    # channel_output = int(message_pair.channel_output)
    print('couldnt get env')
    # channel_output = message_pair.channel_output

# test variable to override channel input from db
pair_name = message_pair.pair_name
client = TelegramClient("BST_t", api_id, api_hash)

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


# @client.on(events.NewMessage)
# async def fresh_message(event):
#     text = event.message.text
client.start()
client.run_until_disconnected()

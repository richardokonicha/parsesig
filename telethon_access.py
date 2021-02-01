from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.channels import GetMessagesRequest
import logging
import redis
from text_parser import pasig
from datetime import datetime
from config import api_hash, api_id, channel_input, channel_output, session, save_session, REDISTOGO_URL
# from util import bot_forward
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

r = redis.from_url(url=REDISTOGO_URL)
client = TelegramClient(StringSession(session), api_id, api_hash)

# client event handler on incoming new messages matching the regex filter from chat or channel
# function takes message text that matches the regex filter and 
# transforms using pasig transformer and sends to output channel
@client.on(
    events.NewMessage(
        chats= channel_input, 
        # pattern=r"^(BUY|SELL)\s([A-Z]*)\s[\(@at\s]*([0-9]*[.,][0-9]*)[\).]", 
        incoming=True,
        ))
async def forwarder(event):
    text = event.message.text
    signal = pasig(text)
    if bool(signal):
        pass
    else:
        signal = text

    message_id = event.message.id
    reply_msg = event.message.reply_to_msg_id

    try:
        ref = int(r.get(reply_msg).decode('utf-8'))
    except:
        print('Out of scope or bounds for redis')
        ref = None

    output_channel = await client.send_message(channel_output, signal, reply_to = ref)
    r.set(event.message.id, output_channel.id)
    print(signal)

# keeps heroku from falling asleep
@client.on(events.NewMessage)
async def wakeup(event):
    text = event.message.text
    # print(text)

client.start()
save_session(client, session)
client.run_until_disconnected()
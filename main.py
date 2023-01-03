import logging
from datetime import datetime
import sentry_sdk
sentry_sdk.init(
    dsn="https://99d6c429276948bd9e71cf6c80d91885@o4504248900583424.ingest.sentry.io/4504248905236480",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

import redis
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.channels import GetMessagesRequest
from config import (REDIS_URL, api_hash, api_id, channel_input,
                    channel_output, session)
from text_parser import emanuelefilter, transform_text
from datetime import datetime   
import time
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

r = redis.from_url(url=REDIS_URL)
client = TelegramClient(StringSession(session), api_id, api_hash)


@client.on(
    events.NewMessage(
        chats= channel_input, 
        incoming=True,
        outgoing=True
        ))
async def forwarder(event):
    text = event.message.text
    message_id = event.message.id
    reply_msg = event.message.reply_to_msg_id
    valid = emanuelefilter(text)
    text = transform_text(text)
    count = 0
    for cht in channel_output:
        try:
            ref = int(r.get(f"{cht}-{reply_msg}").decode('utf-8'))
        except:
            print('Out of scope or bounds for redis')
            ref = None
        try:
            msg_file = event.message.file.media
            ext = event.message.file.ext
        except:
            msg_file = None
            ext = None

        count += 1
      
        print(cht, count)

        if valid:
            try:
                output_channel = await client.send_message(cht, text, file=msg_file, reply_to=ref)
                r.set(f"{cht}-{event.message.id}", output_channel.id)
                print(f"\u001b[32mSENT......{text}....SENT\u001b[37m....")
            except ConnectionRefusedError:
                print(f"\u001b[31mRedis broke\u001b[37m...") 
            except Exception as e:
                print(f"\u001b[31mNot Sent an error occurred {text[:70]} ...Not Sent {e}\u001b[37m...") 
        else:
            print(f"\u001b[31mNot Sent invalid {text[:70]} ...Not Sent\u001b[37m...") 

@client.on(events.NewMessage)
async def wakeup(event):
    print('Active...')

client.start()
client.run_until_disconnected()

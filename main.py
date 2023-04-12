# from text_parser import emanuelefilter, transform_text
import time
# from ben_filter import parse_message
from config import (REDIS_URL, api_hash, api_id, channel_input,
                    channel_output, session, sentry_env)
from telethon.tl.functions.channels import GetMessagesRequest
from telethon.sessions import StringSession
from telethon import TelegramClient, events
import redis
import logging
from datetime import datetime
import sentry_sdk
import re
sentry_sdk.init(
    dsn=sentry_env,
    traces_sample_rate=1.0
)

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

r = redis.from_url(url=REDIS_URL)
client = TelegramClient(StringSession(session), api_id, api_hash)


@client.on(
    events.NewMessage(
        chats=channel_input,
        incoming=True,
        outgoing=True
    ))
async def forwarder(event):
    try:
        text = event.message.text
        message_id = event.message.id
        reply_msg = event.message.reply_to_msg_id

        # cleaned_text = parse_message(text)
        valid = bool(text)
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
                    output_channel = await client.send_message(cht, cleaned_text, file=msg_file, reply_to=ref)
                    print(
                        f"\u001b[32mSENT......{cleaned_text}....SENT\u001b[37m....")
                    r.set(f"{cht}-{event.message.id}", output_channel.id)
                except redis.exceptions.ConnectionError as e:
                    print(f"\u001b[31mRedis broke\u001b[37m...", e)
                except Exception as e:
                    print(
                        f"\u001b[31mNot Sent an error occurred {text[:min(len(text), 50)]} ...Not Sent {e}\u001b[37m...")
            else:
                print(
                    f"\u001b[31mNot Sent invalid {text[:min(len(text), 50)]} ...Not Sent\u001b[37m...")
    except Exception as e:
        print("Ignored message", e)


@ client.on(events.NewMessage)
async def wakeup(event):
    print('Active...')

client.start()
client.run_until_disconnected()

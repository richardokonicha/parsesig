from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.channels import GetMessagesRequest
import logging
import redis
from text_parser import emanuelefilter, transform_text
from datetime import datetime
import time
from config import api_hash, api_id, channel_input, chinput, channel_output, session, sentry_env, REDIS_URL
import sentry_sdk

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
        # pattern=r"^(BUY|SELL)\s([A-Z]*)\s[\(@at\s]*([0-9]*[.,][0-9]*)[\).]",
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
            if event.chat_id in channel_input:
                if str(cht) == '-1001306355077':
                    print("Sending to special destination 1001306355077")
                    if str(event.chat_id) == str(chinput):
                        try:
                            output_channel = await client.send_message(cht, text, file=msg_file, reply_to=ref)
                            r.set(f"{cht}-{event.message.id}", output_channel.id)
                            print(f"\u001b[32mSENT to {cht}: {text}....SENT\u001b[37m....")
                        except redis.exceptions.ConnectionError as e:
                            print(f"\u001b[31mRedis broke\u001b[37m...", e)
                        except Exception as e:
                            print(
                                f"\u001b[31mNot Sent an error occurred {text[:min(len(text), 50)]} ...Not Sent {e}\u001b[37m...")
                else:
                    try:
                        output_channel = await client.send_message(cht, text, file=msg_file, reply_to=ref)
                        r.set(f"{cht}-{event.message.id}", output_channel.id)
                        print(f"\u001b[32mSENT to {cht}: {text}....SENT\u001b[37m....")
                    except redis.exceptions.ConnectionError as e:
                        print(f"\u001b[31mRedis broke\u001b[37m...", e)
                    except Exception as e:
                        print(
                    f"\u001b[31mNot Sent an error occurred {text[:min(len(text), 50)]} ...Not Sent {e}\u001b[37m...")
            else:
                print(
                    f"\u001b[31mNot Sent invalid {text[:min(len(text), 50)]} ...Not Sent\u001b[37m...")
        else:
            print(
                f"\u001b[31mNot Sent invalid {text[:min(len(text), 50)]} ...Not Sent\u001b[37m...")


@client.on(events.NewMessage)
async def wakeup(event):
    print('..')

client.start()
client.run_until_disconnected()

from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os
from dotenv import load_dotenv
from telethon_access import api_id, api_hash
load_dotenv()

_session = os.getenv("port_session")
_client = TelegramClient(StringSession(_session), api_id, api_hash)

async def porter(signal):
    # user = await _client.get_entity(signal)
    print("porter")
    return user


# _client.start()
# value = _client.loop.run_until_complete(porter())

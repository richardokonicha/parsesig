from telethon import TelegramClient
from config import (api_hash, api_id, channel_input,
                    channel_output, session)
from telethon.sessions import StringSession

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.


from telethon.sync import TelegramClient, events

with TelegramClient(StringSession(session), api_id, api_hash) as client:
   for dialog in client.iter_dialogs():
         print(dialog.name, dialog.id)


#    @client.on(events.NewMessage(pattern='(?i).*Hello'))
#    async def handler(event):
#       await event.reply('Hey!')

   client.run_until_disconnected()

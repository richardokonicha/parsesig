from telethon import TelegramClient
from config import (api_hash, api_id, channel_input,
                    channel_output, session)
from telethon.sessions import StringSession
import re

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.


from telethon.sync import TelegramClient, events

with TelegramClient(StringSession("----="), api_id, api_hash) as client:

    for dialog in client.iter_dialogs():
        if re.search("ABI", dialog.name):
            print(dialog.name, dialog.id)

    #    @client.on(events.NewMessage(pattern='(?i).*Hello'))
    #    async def handler(event):
    #       await event.reply('Hey!')

    client.run_until_disconnected()

# '1BJWap1wBu4JXLwyoz7J-VCPEwX9Jwv1uSz5qatBtuJ0C04vh1Zw7dRph1r4IfLC3qhxY7DrtvLMovgvnl2EHqdNE4A1fDIUjdhoCVwUyANKsFq9QCg4xDnoNmnbN-NYoi0JpICXdw1vnM_6-5Wfb00snVJqdPGCjfhLUyfJWFGeFa7apNpC2bKE8qA8bPc7wqWuhUE5muEVQX7C9oUToV65w3H2h_qRCIAKiSF72kpZzWinMzJWNihpAv68dEQ_cpx0XUpgX4gOgvazzKE98mV8Wmd39nms_LHGFfpUF-cghLu_PrJVGrICoMTqWpfRxpXWA1kxPOAOAh_mvhZmNBTUazQEMsn4='

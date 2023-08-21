from telethon import TelegramClient
from config import (api_hash, api_id, channel_input,
                    channel_output, session)
from telethon.sessions import StringSession
import re

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.


from telethon.sync import TelegramClient, events

with TelegramClient(StringSession(""), api_id, api_hash) as client:

    for dialog in client.iter_dialogs():
        if re.search("FX Channel Signal", dialog.name):
            print(dialog.name, dialog.id)

    #    @client.on(events.NewMessage(pattern='(?i).*Hello'))
    #    async def handler(event):
    #       await event.reply('Hey!')

    client.run_until_disconnected()

# '1BJWap1wBu4JXLwyoz7J-VCPEwX9Jwv1uSz5qatBtuJ0C04vh1Zw7dRph1r4IfLC3qhxY7DrtvLMovgvnl2EHqdNE4A1fDIUjdhoCVwUyANKsFq9QCg4xDnoNmnbN-NYoi0JpICXdw1vnM_6-5Wfb00snVJqdPGCjfhLUyfJWFGeFa7apNpC2bKE8qA8bPc7wqWuhUE5muEVQX7C9oUToV65w3H2h_qRCIAKiSF72kpZzWinMzJWNihpAv68dEQ_cpx0XUpgX4gOgvazzKE98mV8Wmd39nms_LHGFfpUF-cghLu_PrJVGrICoMTqWpfRxpXWA1kxPOAOAh_mvhZmNBTUazQEMsn4='
# alberto# '1BJWap1sBuzNXi6lXRGZn-niecVh137ejqerX_yZtSI-r8-O5uvPpIXFCfkED6ZK-z88RPJRjsqsBLlePedPv1ycRZZhEBku8h84J4jr53t0bPTwPK8VzGW-FOEwddrdoGTKYf_LhGHI8F9HGu8S61Fi-bvYUrLFCQY4_siaT0UdhqwqDu7Hh5u7rwHQqmRLztQHtrNmdJL3HyrGphZjXKk_HeMLHjWP62DNZgAMlzzTAKKidB13sPG4mwMKJ6ooTNrVLRbfVhngH75RRvOiQwxPQHTxjdPiXgvOZLI6ftn83-mkIz5guisN4pUL_MB7XhByo9BLO4IGjworkNTK8BprRk9inwzU='


# '1BJWap1sBu4qRoqbsaBUd06KAlnD-3UbaJxG8GMHrZ1Hv7XE0ZEyiX0OFUVubWkPdvNYSWK0VK4wElpJ0xVxpcYQZaZrqE9pASvqA1El3VDn9yDrn413iE13a7QBQyQqhSsxOGJm67nmFYH8l_8BE5LC-YbmBKGsFomtZTv8DZqzXOCa2iMIcpEnMNIVV31Q3eXrNe-WbCOUE4GLlx0M5npJNaAYM7xIimS1PBMo-_cJapSf16L3nTQgqYNpRwr_HgMoLratyKuXvKAZ6riCYJtHdKA9CyHStOnKzRoOVXHQH9duea6QxJ2oSpuiwdakwUbjMEYtFSONWeiKgpWmQaVIaZ-bdBzw='



# '1BJWap1wBu6NjgbVY-yY881W-xDdhrVrUJOmlgQRN5y-sjOZ-E1NDa1-JnfL-_hPfR5hxIjc_MMuJN4ibrQggOrALISbMSi27qY23eJyurncHPxQlN1KVfzuW40aTzHaHhT6cj07epxKAhzj5Q6ict5JvMA_aYw-pt_tBgagx2zQUFA0baePn5CjqmaLIvo9fwtaY-O7SpcWttZJpZpBQu9d5uKJfgkcKiqDJ5SrBe-aHjFgiGgav4v79CzNdXz57o0m5LCEq-RdiH_MEBxgC5C1eQEYBr8gWZagfYWIMk4FLVZUUbbduz1rxXRMJzMtMAbgatnrhWubnnWNHNHCgO0bOUusr_3E='

# '1BJWap1wBuxrhCrFKV0-Ptty-6yA5E7nOHqZZC2nonVibbjoHpNFtoaxip3JoS9PBSMR2K3oTSXw2i4mw44K0unefQYkJJW2vnzUEh2IkThfZ7ulXmTd8yR6jCAVRFvfuQmbMGdcoCwLoXuSHpJKSq5e-xTdR8xZrTHkITWYJcAlqsDUvdNbb-Xf9p6MgDeU2XTfAz97gQPj6lpDX-KQfXlY-7oGN0iFd0zYdiYHWAbFkvpiOQZqqx9y8-L4EM9MiJyMsqN7QJ90EIFBt6g1RiY3Sy-53sMbjuHPgEfAB1eCvHbldmm3pyM7hktI4Lfn50MMYNgYBtUeID15LJguL9_1FDRAaN2U='
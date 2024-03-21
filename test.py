from telethon import TelegramClient

# Remember to use your own values from my.telegram.org!
# api_id = 1347918
# api_hash = '5681581438678d9390cd4f67ee764f82'
client = TelegramClient('anon', api_id, api_hash)

async def main():
    me = await client.get_me()
    print(me.stringify())
    # You can print all the dialogs/conversations that you are part of:
    async for dialog in client.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)
with client:
    client.loop.run_until_complete(main())

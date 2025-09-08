from ivanxuserbot.core import client
from telethon import events
from ivanxuserbot.utils import get_uptime
@client.on(events.NewMessage(pattern=r'\.stats$'))
async def stats(event):
    me = await client.get_me()
    text = f"**Stats**\nUser: {me.first_name} (`{me.id}`)\nUptime: {get_uptime()}"
    await event.reply(text)
@client.on(events.NewMessage(pattern=r'\.members$'))
async def members(event):
    try:
        count = 0
        async for _ in client.iter_participants(event.chat_id):
            count += 1
        await event.reply(f"👥 Members: {count}")
    except Exception:
        await event.reply('Could not fetch members count.')

from ivanxuserbot.core import client
from telethon import events
import random
@client.on(events.NewMessage(pattern=r'\.couple$'))
async def couple(event):
    chat = await event.get_chat()
    if not getattr(chat, 'megagroup', False) and not getattr(chat, 'title', None):
        return await event.reply('This command works best in groups.')
    participants = []
    async for user in client.iter_participants(event.chat_id):
        if not user.bot:
            participants.append(user)
    if len(participants) < 2:
        return await event.reply('Not enough people to match.')
    p = random.sample(participants, 2)
    u1 = f"[{p[0].first_name}](tg://user?id={p[0].id})"
    u2 = f"[{p[1].first_name}](tg://user?id={p[1].id})"
    await event.reply(f"{u1} ❤️ {u2}\nA perfect match!" )

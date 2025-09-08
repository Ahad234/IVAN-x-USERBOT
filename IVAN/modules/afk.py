from ivanxuserbot.core import client
from telethon import events
AFK = {'status': False, 'reason': None}
@client.on(events.NewMessage(pattern=r'\.afk(?: |$)(.*)'))
async def go_afk(event):
    reason = event.pattern_match.group(1).strip()
    AFK['status'] = True
    AFK['reason'] = reason or 'Away'
    await event.reply(f"🌙 AFK: {AFK['reason']}")
@client.on(events.NewMessage(pattern=r'\.back$'))
async def back(event):
    AFK['status'] = False
    AFK['reason'] = None
    await event.reply('☀️ I am back!')
@client.on(events.NewMessage())
async def afk_auto_reply(event):
    if AFK['status'] and not event.out:
        await event.reply(f"🌙 I'm AFK: {AFK['reason']}")

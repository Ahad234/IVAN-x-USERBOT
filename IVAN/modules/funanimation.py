from ivanxuserbot.core import client
from telethon import events
import asyncio
@client.on(events.NewMessage(pattern=r'\.animation (.+)'))
async def animation(event):
    text = event.pattern_match.group(1)
    m = await event.reply(text[:1])
    for i in range(2, len(text)+1):
        await asyncio.sleep(0.08)
        try:
            await m.edit(text[:i])
        except:
            pass
@client.on(events.NewMessage(pattern=r'\.funanimation$'))
async def funanimation(event):
    await event.reply('✨ Fun animations ready! Use .animation <text> or .type <text>.')
@client.on(events.NewMessage(pattern=r'\.type (.+)'))
async def typewriter(event):
    text = event.pattern_match.group(1)
    m = await event.reply('')
    for i in range(1, len(text)+1):
        await asyncio.sleep(0.05)
        try:
            await m.edit(text[:i])
        except:
            pass
@client.on(events.NewMessage(pattern=r'\.wave (.+)'))
async def wave(event):
    text = event.pattern_match.group(1)
    m = await event.reply(text)
    for _ in range(4):
        await asyncio.sleep(0.2)
        try:
            await m.edit('🌊 ' + text + ' 🌊')
        except:
            pass

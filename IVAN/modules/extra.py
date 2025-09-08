from ivanxuserbot.core import client
from telethon import events
@client.on(events.NewMessage(pattern=r'\.kang$'))
async def kang_alias(event):
    await event.reply('Use .kang in media module for sticker kanging.')

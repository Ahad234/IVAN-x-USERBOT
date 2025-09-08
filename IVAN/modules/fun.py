from ivanxuserbot.core import client
from telethon import events
import asyncio
@client.on(events.NewMessage(pattern=r'\.hack$'))
async def hack(event):
    seq = ["🔍 Initializing hack...","🔐 Bypassing firewall...","📡 Extracting data...","💾 Uploading payload...","✅ Hack complete!"]
    m = await event.reply(seq[0])
    for s in seq[1:]:
        await asyncio.sleep(1)
        await m.edit(s)
@client.on(events.NewMessage(pattern=r'\.raid$'))
async def raid(event):
    # For safety, only owner can run raid and it's friendly (single not spamming)
    from ivanxuserbot.config import OWNER_ID
    if event.sender_id != OWNER_ID:
        return await event.reply('❌ raid is owner-only (disabled for safety).')
    if not event.is_reply:
        return await event.reply('Reply to a user to run raid (owner-only, minimal).')
    target = await event.get_reply_message()
    await event.reply(f"⚠️ Friendly raid on {getattr(target.sender,'first_name',target.sender_id)} (owner-only)." )
@client.on(events.NewMessage(pattern=r'\.raid2$'))
async def raid2(event):
    # same safety policy as raid
    from ivanxuserbot.config import OWNER_ID
    if event.sender_id != OWNER_ID:
        return await event.reply('❌ raid2 is owner-only (disabled for safety).')
    await event.reply('⚠️ Raid2: disabled for safety.')
@client.on(events.NewMessage(pattern=r'\.dmraid$'))
async def dmraid(event):
    # DM raids/spamming is harmful; disabled.
    return await event.reply('❌ dmraid is disabled for safety.')
@client.on(events.NewMessage(pattern=r'\.game$'))
async def game(event):
    await event.reply('🎮 Game time! (not implemented)')

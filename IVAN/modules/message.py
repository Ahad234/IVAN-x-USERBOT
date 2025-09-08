from ivanxuserbot.core import client
from telethon import events
import asyncio
@client.on(events.NewMessage(pattern=r'\.del$'))
async def delete_msg(event):
    if not event.is_reply:
        return await event.reply('Reply to a message to delete it.')
    m = await event.get_reply_message()
    await m.delete()
    await event.delete()
@client.on(events.NewMessage(pattern=r'\.purge(?: |$)(\d+)?'))
async def purge(event):
    count = int(event.pattern_match.group(1) or 20)
    if not event.is_reply:
        return await event.reply('Reply to a message to start purge from there.')
    start_msg = await event.get_reply_message()
    deleted = 0
    async for msg in client.iter_messages(event.chat_id, offset_id=start_msg.id, limit=count):
        try:
            await msg.delete()
            deleted += 1
        except:
            pass
    await event.reply(f'🧹 Purged {deleted} messages.')
@client.on(events.NewMessage(pattern=r'\.pin$'))
async def pin(event):
    if not event.is_reply:
        return await event.reply('Reply to a message to pin.')
    msg = await event.get_reply_message()
    await client.pin_message(event.chat_id, msg.id)
    await event.reply('📌 Message pinned.')
@client.on(events.NewMessage(pattern=r'\.unpin$'))
async def unpin(event):
    await client.unpin_message(event.chat_id)
    await event.reply('📌 Unpinned messages.')
@client.on(events.NewMessage(pattern=r'\.edit (.+)'))
async def edit_msg(event):
    new = event.pattern_match.group(1)
    if not event.is_reply:
        return await event.reply('Reply to a message to edit.')
    msg = await event.get_reply_message()
    try:
        await msg.edit(new)
        await event.delete()
    except Exception as e:
        await event.reply(f"Can't edit: {e}")

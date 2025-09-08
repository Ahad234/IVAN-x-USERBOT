from ivanxuserbot.core import client
from ivanxuserbot.config import OWNER_ID
from telethon import events, errors
from telethon.tl.types import ChatAdminRights
@client.on(events.NewMessage(pattern=r'\.ban$'))
async def ban_user(event):
    if not event.is_reply:
        return await event.reply('Reply to a user to ban.')
    target = await event.get_reply_message()
    try:
        await client.edit_permissions(event.chat_id, target.sender_id, view_messages=False)
        await event.reply('🚫 User banned.')
    except errors.ChatAdminRequiredError:
        await event.reply('I need admin rights to ban.')
@client.on(events.NewMessage(pattern=r'\.unban$'))
async def unban_user(event):
    if not event.is_reply:
        return await event.reply('Reply to a user to unban.')
    target = await event.get_reply_message()
    try:
        await client.edit_permissions(event.chat_id, target.sender_id, view_messages=True)
        await event.reply('✅ User unbanned.')
    except errors.ChatAdminRequiredError:
        await event.reply('I need admin rights to unban.')
@client.on(events.NewMessage(pattern=r'\.kick$'))
async def kick_user(event):
    if not event.is_reply:
        return await event.reply('Reply to a user to kick.')
    target = await event.get_reply_message()
    try:
        await client.kick_participant(event.chat_id, target.sender_id)
        await event.reply('👢 User kicked.')
    except errors.ChatAdminRequiredError:
        await event.reply('I need admin rights to kick.')
@client.on(events.NewMessage(pattern=r'\.promote$'))
async def promote(event):
    if not event.is_reply:
        return await event.reply('Reply to a user to promote.')
    target = await event.get_reply_message()
    try:
        rights = ChatAdminRights(add_admins=False, change_info=True, ban_users=True, invite_users=True, pin_messages=True, manage_call=True)
        await client(functions.channels.EditAdminRequest(event.chat_id, target.sender_id, rights, 'ivanxuserbot'))
        await event.reply('✅ Promoted (attempt).')
    except Exception:
        await event.reply('Promote failed or not supported.')
@client.on(events.NewMessage(pattern=r'\.demote$'))
async def demote(event):
    if not event.is_reply:
        return await event.reply('Reply to a user to demote.')
    target = await event.get_reply_message()
    try:
        await client(functions.channels.EditAdminRequest(event.chat_id, target.sender_id, ChatAdminRights(False,False,False,False,False,False), ''))
        await event.reply('✅ Demoted (attempt).')
    except Exception:
        await event.reply('Demote failed or not supported.')
@client.on(events.NewMessage(pattern=r'\.banall$'))
async def banall(event):
    # Dangerous action — restricted to owner only and requires confirmation
    if event.sender_id != OWNER_ID:
        return await event.reply('❌ Only the owner can run banall (disabled).')
    await event.reply('Banall is disabled for safety.')

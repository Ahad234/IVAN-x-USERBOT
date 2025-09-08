from ivanxuserbot.core import client
from telethon import events
@client.on(events.NewMessage(pattern=r'\.id$'))
async def my_id(event):
    if event.is_reply:
        msg = await event.get_reply_message()
        await event.reply(f"👤 User ID: `{msg.sender_id}`")
    else:
        await event.reply(f"👤 Your ID: `{event.sender_id}`")
@client.on(events.NewMessage(pattern=r'\.userinfo$'))
async def userinfo(event):
    if not event.is_reply:
        return await event.reply('Reply to a user to get info.')
    msg = await event.get_reply_message()
    user = await client.get_entity(msg.sender_id)
    text = f"**User Info**\nName: {getattr(user,'first_name','')} {getattr(user,'last_name','')}\nID: `{user.id}`\nUsername: @{getattr(user,'username','')}"
    await event.reply(text)
@client.on(events.NewMessage(pattern=r'\.whois$'))
async def whois(event):
    await userinfo(event)
@client.on(events.NewMessage(pattern=r'\.chatinfo$'))
async def chatinfo(event):
    chat = await event.get_chat()
    text = f"**Chat Info**\nName: {getattr(chat,'title','Private')}\nID: `{chat.id}`\nType: {type(chat)}"
    await event.reply(text)

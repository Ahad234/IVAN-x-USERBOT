from ivanxuserbot.core import client
from telethon import events
from ivanxuserbot.utils import get_uptime
from ivanxuserbot.config import OWNER_ID
import os, sys, subprocess
@client.on(events.NewMessage(pattern=r'\.help$'))
async def help_cmd(event):
    help_text = """📜 ivanxuserbot Help (main commands)
System: .help .alive .ping .restart .update .logs .stats
Admin: .ban .unban .banall .promote .demote .kick
Message: .del .purge <n> .pin .unpin .edit <text>
Fun: .hack .raid .raid2 .game .couple .animation .funanimation
Media: .screenshot <url> .download .upload .song .photo .sticker .kang
Tools: .gm .echo .reverse .carbon .qrcode .tr
Dev: .eval .exec .term .daveloper
"""
    await event.reply(help_text)
@client.on(events.NewMessage(pattern=r'\.alive$'))
async def alive(event):
    await event.reply("✅ ivanxuserbot is alive!")
@client.on(events.NewMessage(pattern=r'\.ping$'))
async def ping(event):
    m = await event.reply("🏓 Pong!")
@client.on(events.NewMessage(pattern=r'\.restart$'))
async def restart(event):
    if event.sender_id != OWNER_ID:
        return await event.reply("❌ Only owner can restart.")
    await event.reply("♻️ Restarting...")
    os.execv(sys.executable, [sys.executable] + sys.argv)
@client.on(events.NewMessage(pattern=r'\.update$'))
async def update(event):
    if event.sender_id != OWNER_ID:
        return await event.reply("❌ Only owner can update.")
    await event.reply("⬆️ Update: pulling from git... (stub)")
    # Real implementation: git pull, pip install -r requirements, restart.
@client.on(events.NewMessage(pattern=r'\.logs$'))
async def logs(event):
    logfile = 'ivanxuserbot.log'
    if not os.path.exists(logfile):
        return await event.reply('No logs found.')
    await event.reply('📜 Sending logs...')
    await client.send_file(event.chat_id, logfile)
@client.on(events.NewMessage(pattern=r'\.daveloper$'))
async def daveloper(event):
    await event.reply('👨‍💻 Developer: Ivan')

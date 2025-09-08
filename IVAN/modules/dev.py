from ivanxuserbot.core import client
from ivanxuserbot.config import OWNER_ID
from telethon import events
import subprocess, asyncio
def owner_only(func):
    async def wrapper(event):
        if event.sender_id != OWNER_ID:
            return await event.reply('❌ Only owner can use this.')
        return await func(event)
    return wrapper
@client.on(events.NewMessage(pattern=r'\.eval (.+)'))
@owner_only
async def eval_cmd(event):
    code = event.pattern_match.group(1)
    try:
        result = eval(code, {'client': client, '__name__': '__main__'})
        await event.reply(f"✅ Result:\n`{result}`")
    except Exception as e:
        await event.reply(f"❌ Error: {e}")
@client.on(events.NewMessage(pattern=r'\.exec (.+)'))
@owner_only
async def exec_cmd(event):
    cmd = event.pattern_match.group(1)
    try:
        proc = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=30)
        out = proc.stdout or proc.stderr or 'No output'
        if len(out) > 4000:
            out = out[:4000] + '\n...(truncated)'
        await event.reply(f"📜 Output:\n`{out}`")
    except Exception as e:
        await event.reply(f"❌ Error: {e}")
@client.on(events.NewMessage(pattern=r'\.term (.+)'))
@owner_only
async def term_cmd(event):
    await exec_cmd(event)
@client.on(events.NewMessage(pattern=r'\.daveloper$'))
async def daveloper(event):
    await event.reply('👨‍💻 Developer: Ivan')

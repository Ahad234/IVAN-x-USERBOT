from ivanxuserbot.core import client
from telethon import events
STARTUP_BANNER = "🚀 ivanxuserbot Started! Type `.help` to see commands."
@client.on(events.NewMessage(pattern=r"/start"))
async def start_cmd(event):
    await event.reply("👋 Hi! I am running on your account. Type `.help` for commands.")
async def send_startup_banner():
    try:
        me = await client.get_me()
        await client.send_message(me.id, STARTUP_BANNER)
    except Exception:
        pass

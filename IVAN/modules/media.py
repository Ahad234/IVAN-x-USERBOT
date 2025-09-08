from ivanxuserbot.core import client
from telethon import events
import aiohttp, os
from io import BytesIO
from PIL import Image
@client.on(events.NewMessage(pattern=r'\.screenshot (.+)'))
async def screenshot(event):
    url = event.pattern_match.group(1).strip()
    await event.reply(f"📸 Capturing {url} ...")
    try:
        async with aiohttp.ClientSession() as s:
            async with s.get(f"https://image.thum.io/get/{url}") as resp:
                if resp.status == 200:
                    data = await resp.read()
                    await client.send_file(event.chat_id, BytesIO(data), caption=f"Screenshot of {url}")
                else:
                    await event.reply('Failed to get screenshot.')
    except Exception as e:
        await event.reply(f'Error: {e}')
@client.on(events.NewMessage(pattern=r'\.download$'))
async def download_media(event):
    if not event.is_reply:
        return await event.reply('Reply to a media message to download.')
    msg = await event.get_reply_message()
    if not msg.media:
        return await event.reply('No media found.')
    path = await client.download_media(msg.media)
    await event.reply(f'Saved to `{path}`')
@client.on(events.NewMessage(pattern=r'\.upload (.+)'))
async def upload_file(event):
    path = event.pattern_match.group(1).strip()
    if not os.path.exists(path):
        return await event.reply('File not found.')
    await client.send_file(event.chat_id, path)
@client.on(events.NewMessage(pattern=r'\.sticker$'))
async def send_sticker(event):
    # send a placeholder sticker/file if exists
    f = 'sample.webp'
    if os.path.exists(f):
        await client.send_file(event.chat_id, f)
    else:
        await event.reply('No sticker file found.')
@client.on(events.NewMessage(pattern=r'\.kang$'))
async def kang(event):
    if not event.is_reply:
        return await event.reply('Reply to an image to kang as sticker.')
    msg = await event.get_reply_message()
    if not msg.media:
        return await event.reply('Reply to an image.')
    # download to bytes, convert to webp and send as sticker
    data = await client.download_media(msg.media, file=BytesIO())
    try:
        img = Image.open(data).convert('RGBA')
        out = BytesIO()
        img.save(out, format='WEBP', lossless=True, quality=80, method=6)
        out.seek(0)
        await client.send_file(event.chat_id, out, force_document=False, allow_cache=False)
        await event.reply('✅ Sticker kanged (basic).')
    except Exception as e:
        await event.reply(f'Failed to kang: {e}')

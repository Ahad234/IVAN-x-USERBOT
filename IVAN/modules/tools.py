from ivanxuserbot.core import client
from telethon import events
import qrcode
from io import BytesIO
@client.on(events.NewMessage(pattern=r'\.gm$'))
async def gm(event):
    await event.reply('🌞 Good Morning!')
@client.on(events.NewMessage(pattern=r'\.echo (.+)'))
async def echo(event):
    await event.reply(event.pattern_match.group(1))
@client.on(events.NewMessage(pattern=r'\.reverse (.+)'))
async def reverse(event):
    await event.reply(event.pattern_match.group(1)[::-1])
@client.on(events.NewMessage(pattern=r'\.upper (.+)'))
async def upper(event):
    await event.reply(event.pattern_match.group(1).upper())
@client.on(events.NewMessage(pattern=r'\.lower (.+)'))
async def lower(event):
    await event.reply(event.pattern_match.group(1).lower())
@client.on(events.NewMessage(pattern=r'\.qrcode (.+)'))
async def make_qr(event):
    data = event.pattern_match.group(1)
    buf = BytesIO()
    qrcode.make(data).save(buf, format='PNG')
    buf.seek(0)
    await client.send_file(event.chat_id, buf, caption='QR code')
@client.on(events.NewMessage(pattern=r'\.carbon (.+)'))
async def carbon(event):
    # simple carbon-like image from text
    from PIL import Image, ImageDraw, ImageFont
    text = event.pattern_match.group(1)
    try:
        font = ImageFont.load_default()
        lines = text.split('\n')
        width = max([font.getsize(l)[0] for l in lines]) + 20
        height = (font.getsize(lines[0])[1] * len(lines)) + 20
        img = Image.new('RGBA', (width, height), (40,44,52,255))
        draw = ImageDraw.Draw(img)
        y = 10
        for l in lines:
            draw.text((10,y), l, font=font, fill=(255,255,255,255))
            y += font.getsize(l)[1]
        buf = BytesIO()
        img.save(buf, format='PNG')
        buf.seek(0)
        await client.send_file(event.chat_id, buf, caption='carbon image')
    except Exception as e:
        await event.reply(f'Carbon failed: {e}')

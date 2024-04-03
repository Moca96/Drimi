import glob
import io
import os
import random

import requests
from PIL import Image, ImageDraw, ImageFont

from FallenRobot import BOT_NAME, BOT_USERNAME, OWNER_ID, telethn
from FallenRobot.events import register

LOGO_LINKS = [
    "https://telegra.ph/file/152e0a0a9c208950d455f.jpg",
    "https://telegra.ph/file/43957afb78ee835103139.jpg",
    "https://telegra.ph/file/8f534e09d999bbafb1c1f.jpg",
]


@register(pattern="^/logo ?(.*)")
async def lego(event):
    quew = event.pattern_match.group(1)
    if event.sender_id != OWNER_ID and not quew:
        await event.reply(
            "ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴄʀᴇᴀᴛᴇ ʟᴏɢᴏ !\nExample : `/logo <ANONYMOUS>`"
        )
        return
    pesan = await event.reply("**ᴄʀᴇᴀᴛɪɴɢ ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛᴇᴅ ʟᴏɢᴏ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ᴀ sᴇᴄ...**")
    try:
        text = event.pattern_match.group(1)
        randc = random.choice(LOGO_LINKS)
        img = Image.open(io.BytesIO(requests.get(randc).content))
        draw = ImageDraw.Draw(img)
        image_widthz, image_heightz = img.size
        fnt = glob.glob("./FallenRobot/resources/fonts/*")
        randf = random.choice(fnt)
        font = ImageFont.truetype(randf, 120)
        lw, th, rw, bh = font.getbbox(text)
        w, h = rw - lw, bh - th
        h += int(h * 0.21)
        image_width, image_height = img.size
        draw.text(
            ((image_widthz - w) / 2, (image_heightz - h) / 2),
            text,
            font=font,
            fill=(255, 255, 255),
        )
        x = (image_widthz - w) / 2
        y = (image_heightz - h) / 2 + 6
        draw.text(
            (x, y), text, font=font, fill="white", stroke_width=1, stroke_fill="black"
        )
        fname = "fallen.png"
        img.save(fname, "png")
        await telethn.send_file(
            event.chat_id,
            file=fname,
            caption=f"ʟᴏɢᴏ ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ [{BOT_NAME}](https://t.me/{BOT_USERNAME})",
        )
        await pesan.delete()
        if os.path.exists(fname):
            os.remove(fname)
    except Exception:
        text = event.pattern_match.group(1)
        randc = random.choice(LOGO_LINKS)
        img = Image.open(io.BytesIO(requests.get(randc).content))
        draw = ImageDraw.Draw(img)
        image_widthz, image_heightz = img.size
        fnt = glob.glob("./FallenRobot/resources/fonts/*")
        randf = random.choice(fnt)
        font = ImageFont.truetype(randf, 120)
        lw, th, rw, bh = font.getbbox(text)
        w, h = rw - lw, bh - th
        h += int(h * 0.21)
        image_width, image_height = img.size
        draw.text(
            ((image_widthz - w) / 2, (image_heightz - h) / 2),
            text,
            font=font,
            fill=(255, 255, 255),
        )
        x = (image_widthz - w) / 2
        y = (image_heightz - h) / 2 + 6
        draw.text(
            (x, y), text, font=font, fill="white", stroke_width=1, stroke_fill="black"
        )
        fname = "fallen.png"
        img.save(fname, "png")
        await telethn.send_file(
            event.chat_id,
            file=fname,
            caption=f"ʟᴏɢᴏ ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ [{BOT_NAME}](https://t.me/{BOT_USERNAME})",
        )
        await pesan.delete()
        if os.path.exists(fname):
            os.remove(fname)


__mod_name__ = "Lᴏɢᴏ"

__help__ = """
I can create some beautiful and attractive logo for your profile pics.

❍ /logo <text>*:* Create a logo of your given text with random view.
"""

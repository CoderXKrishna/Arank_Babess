import asyncio
from platform import python_version as pyver

from pyrogram import __version__ as pver
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as lver
from telethon import __version__ as tver

from ArankBabess import SUPPORT_CHAT, pbot,BOT_USERNAME, OWNER_ID

PHOTO = [
    "https://telegra.ph/file/e96afa43e300cd6a952cd.jpg",
    "https://telegra.ph/file/36caf45b45a45ea368434.jpg",
    "https://telegra.ph/file/a54767f825a665a136aa3.mp4",
    "https://telegra.ph/file/ac9738d48c92068580a9f.jpg",
    "https://telegra.ph/file/ac9738d48c92068580a9f.jpg",
]

Arank = [
    [
        InlineKeyboardButton(text="📍𝐎𝐰𝐧𝐞𝐫📍", url=f"tg://user?id={OWNER_ID}"),
        InlineKeyboardButton(text="🍒𝐆𝐫𝐨𝐮𝐩🍒", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
    [
        InlineKeyboardButton(
            text="☆ 𝐀𝐝𝐝 𝐌𝐞 𝐌𝐨𝐢 𝐋𝐮𝐯 ☆",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

lol = "https://telegra.ph/file/58f52417365f7f8622e02.jpg"


@pbot.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("⚡")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ..")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ......")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ..")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ......")
    await accha.delete()
    await asyncio.sleep(0.5)
    umm = await m.reply_sticker(
        "CAACAgUAAxkDAAJHbmLuy2NEfrfh6lZSohacEGrVjd5wAAIOBAACl42QVKnra4sdzC_uKQQ"
    )
    await umm.delete()
    await asyncio.sleep(0.8)
    await m.reply_photo(
        lol,
        caption=f"""**🌷ʜᴇʏ, ɪ ᴀᴍ 『[𝗩𝗜𝗣 𝗥𝗢𝗕𝗢𝗧](f"t.me/{BOT_USERNAME}")』🎄**
   ╔═════ஜ۩۞۩ஜ════╗

   ♨️𝗠𝗔𝗗𝗘 𝗕𝗬 [Arank](https://t.me/Arank_Music)♨️

   ╚═════ஜ۩۞۩ஜ════╝""",
        reply_markup=InlineKeyboardMarkup(Arank),
    )
__mod_name__ = "♨️ᴀʟɪᴠᴇ♨️"
__help__ = """

*ᴜsᴇʀ ᴄᴏᴍᴍᴀɴᴅs*:
» /alive*:* ᴛᴏ ᴄʜᴇᴀᴋ ❓  ɪ ᴀᴍ ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ?

☆............𝙱𝚈 » [Arank](https://t.me/Arank_Music)............☆"""

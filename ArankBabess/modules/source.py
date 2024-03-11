from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from ArankBabess import OWNER_ID, dispatcher
from ArankBabess import pbot as client

Arank = "https://telegra.ph/file/e96afa43e300cd6a952cd.jpg"


@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=Arank,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [{dispatcher.bot.first_name}](t.me/{dispatcher.bot.username})**

╔═════ஜ۩۞۩ஜ════╗

 ♨️𝗠𝗔𝗗𝗘 𝗕𝗬 [ᴋᴀɴɪꜱʜᴋᴀ ᴍᴀɴᴀɢᴍᴇɴᴛ](https://t.me/Itsz_Kanishka_Babess)♨️
  
╚═════ஜ۩۞۩ஜ════╝

**[ᴋᴀɴɪꜱʜᴋᴀ ᴍᴀɴᴀɢᴍᴇɴᴛ](t.me/{dispatcher.bot.username}) sᴏᴜʀᴄᴇ ɪs ɴᴏᴡ ᴩᴜʙʟɪᴄ ᴀɴᴅ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📍ᴏᴡɴᴇʀ📍",f"tg://user?id={OWNER_ID}"
                    ),
                    InlineKeyboardButton(
                        "📍ʀᴇᴘᴏ📍",
                        url="https://github.com/CoderXKrishna/Arank_Babess",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "⚡Rᴇᴩᴏ⚡"
_help__ = """
 /repo  ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ 
 /source ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ
"""

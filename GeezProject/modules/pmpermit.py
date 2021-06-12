# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pyrogram import Client
import asyncio
from GeezProject.config import SUDO_USERS, PMPERMIT, OWNER, PROJECT_NAME, UPDATES_CHANNEL, SUPPORT_GROUP
from pyrogram import filters
from pyrogram.types import Message
from GeezProject.services.callsmusic.callsmusic import client as USER

PMSET =True
pchats = []

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE":
        if PMSET:
            chat_id = message.chat.id
            if chat_id in pchats:
                return
            await USER.send_message(
                message.chat.id,
                f"☬ 𝙈𝙪𝙨𝙞𝙘 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩 - 𝙁𝙃 𝙈𝙐𝙎𝙄𝙆 ☬\nThis is a music service of @fhmusikbot\n┏━━━━━━━━━━━━━━━━━━━━━\n ✦҈͜͡➳ Not a place to chat.\n ✦҈͜͡➳ Don't spam in here.\n ✦҈͜͡➳ Don't share private info in here.\n┗━━━━━━━━━━━━━━━━━━━━━\n\nManaged by : @paatriick",
            )
            return

    

@Client.on_message(filters.command(["/pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("**Pmpermit dinyalakan**")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("**Pmpermit dimatikan**")
            return

@USER.on_message(filters.text & filters.private & filters.me)        
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("Disetujui untuk Private Message")
        return
    message.continue_propagation()    
    
@USER.on_message(filters.command("yes", [".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("Disetujui untuk Private Message")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("no", [".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("Maaf anda Ditolak untuk Private Message")
        return
    message.continue_propagation()    

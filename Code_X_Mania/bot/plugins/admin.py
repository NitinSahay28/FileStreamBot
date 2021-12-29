# (c) @AbirHasan2005

import shutil
import psutil
from pyrogram import filters
from pyrogram.types import Message
from Code_X_Mania.vars import Var
from Code_X_Mania.bot import StreamBot
from Code_X_Mania.database import db
from Code_X_Mania.utils.human_readable import humanbytes
from Code_X_Mania.utils.broadcast import send_msg
import time
import string
import random
import asyncio
import datetime
import aiofiles
import traceback
import aiofiles.os
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid
broadcast_ids = {}
@StreamBot.on_message(filters.command("status") & ~filters.edited)
async def status_handler(_, m: Message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    total_users = await db.total_users_count()
    await m.reply_text(
        text=f"**Total Disk Space:** {total} \n"
             f"**Used Space:** {used}({disk_usage}%) \n"
             f"**Free Space:** {free} \n"
             f"**CPU Usage:** {cpu_usage}% \n"
             f"**RAM Usage:** {ram_usage}%\n\n"
             f"**Total Users in DB:** `{total_users}`",
        parse_mode="Markdown",
        quote=True
    )



from pyrogram.types import InlineKeyboardButton

import config
from RDXMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="˹sᴜᴍᴍᴏɴ ᴍє˼", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="˹sᴜᴘᴘ๏ʀᴛ˼", url="https://t.me/JaAT_CoM_303"),
        ],
        [
            InlineKeyboardButton(
                text="˹ᴜᴘᴅᴀᴛᴇs˼",
                url="https://t.me/StUdY_302"
            ),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            
            InlineKeyboardButton(text= "˹ʜєʟᴘ & ᴄᴍᴅ˼", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="˹sᴜᴘᴘ๏ʀᴛ˼",
                url="https://t.me/JaAT_CoM_303"),
            InlineKeyboardButton(
                text="˹sᴜᴘᴘ๏ʀᴛ˼", 
                url="https://t.me/JaAT_CoM_303"),],[
            InlineKeyboardButton(text="˹sᴜᴍᴍᴏɴ ᴍє ʙᴀʙʏ˼", url=f"https://t.me/{app.username}?startgroup=true",),],
        [
            InlineKeyboardButton(text="˹๏ᴡɴєʀ˼", user_id="6441126161"),
            InlineKeyboardButton(text="˹ᴜᴘᴅᴀᴛєѕ˼", url="https://t.me/StUdY_302"),
        ],
    ]
    return buttons


def cmd_panel(_):
    buttons = [
        [
            
            InlineKeyboardButton(text= "˹ʜєʟᴘ & ᴄᴍᴅ˼", callback_data="CMDPANEL1"
            ),
        ],
        [
            InlineKeyboardButton(
                text="˹sᴜᴘᴘ๏ʀᴛ˼",
                url="https://t.me/JaAT_CoM_303"),
            InlineKeyboardButton(
                text="˹sᴜᴘᴘ๏ʀᴛ˼", 
                url="https://t.me/JaAT_CoM_303"),],[
            InlineKeyboardButton(text="˹sᴜᴍᴍᴏɴ ᴍє ʙᴀʙʏ˼", url=f"https://t.me/{app.username}?startgroup=true",),],
        [
            InlineKeyboardButton(text="˹๏ᴡɴєʀ˼", user_id="6441126161"),
            InlineKeyboardButton(text="˹ᴜᴘᴅᴀᴛєѕ˼", url="https://t.me/StUdY_302"),
        ],
    ]
    return buttons




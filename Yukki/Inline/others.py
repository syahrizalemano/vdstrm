from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from Yukki import db_mem


def others_markup(videoid, user_id):
    if videoid not in db_mem:
        db_mem[videoid] = {}
    db_mem[videoid]["check"] = 1
    buttons = [
        [
            InlineKeyboardButton(
                text="🔎 𝑪𝒂𝒓𝒊 𝑳𝒊𝒓𝒊𝒌",
                callback_data=f"lyrics {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝑨𝒅𝒅 𝑻𝒐 𝑷𝒍𝒂𝒚𝒍𝒊𝒔𝒕",
                callback_data=f"your_playlist {videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="𝑨𝒅𝒅 𝑮𝒓𝒐𝒖𝒑 𝑷𝒍𝒂𝒚𝒍𝒊𝒔𝒕",
                callback_data=f"group_playlist {videoid}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬇️𝑫𝒐𝒘𝒏𝒍𝒐𝒂𝒅 𝑨𝒖𝒅𝒊𝒐/𝑽𝒊𝒅𝒆𝒐",
                callback_data=f"audio_video_download {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(
                text="⬅️𝑲𝒆𝒎𝒃𝒂𝒍𝒊",
                callback_data=f"pr_go_back_timer {videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="🗑 𝑪𝒍𝒐𝒔𝒆 𝑴𝒆𝒏𝒖",
                callback_data=f"close",
            ),
        ],
    ]
    return buttons


def download_markup(videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="🎵",
                callback_data=f"gets audio|{videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="🎥",
                callback_data=f"gets video|{videoid}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝑲𝒆𝒎𝒃𝒂𝒍𝒊", callback_data=f"goback {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="🗑 Close Menu", callback_data=f"close"),
        ],
    ]
    return buttons

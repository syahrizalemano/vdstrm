from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from config import MUSIC_BOT_NAME, SUPPORT_CHANNEL, SUPPORT_GROUP
from Yukki import BOT_USERNAME


def setting_markup2():
    buttons = [
        [
            InlineKeyboardButton(text="ð Audio Quality", callback_data="AQ"),
            InlineKeyboardButton(text="ð Audio Volume", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="ð¥ Authorized Users", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="ð» Dashboard", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="âï¸ Close", callback_data="close"),
        ],
    ]
    return f"ð§  **{MUSIC_BOT_NAME} Settings**", buttons


def start_pannel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="ð Helper Commands Menu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ð§ Settings", callback_data="settingm"
                )
            ],
        ]
        return f"ð  **This is {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="ð Helper Commands Menu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ð§ Settings", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="ð¨IDNS Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"ð  **This is {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="ð Helper Commands Menu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ð§ Settings", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="ð¨IDNS Channel", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"ð  **This is {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="ð Helper Commands Menu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ð§ Settings", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="ð¨IDNS Channel", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="ð¨IDNS Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"ð  **This is {MUSIC_BOT_NAME}**", buttons


def private_panel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="ð Helper Commands Menu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "â Add me to your Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
        ]
        return f"ð  **This is {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="ð Helper Commands Menu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "â Add me to your Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="ð¨IDNS Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"ð  **This is {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="ð Helper Commands Menu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "â Add me to your Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="ð¨IDNS Channel", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"ð  **This is {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="ð Helper Commands Menu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "â Add me to your Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="ð¨IDNS Channel", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="ð¨IDNS Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"ð  **This is {MUSIC_BOT_NAME}**", buttons


def setting_markup():
    buttons = [
        [
            InlineKeyboardButton(text="ð Audio Quality", callback_data="AQ"),
            InlineKeyboardButton(text="ð Audio Volume", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="ð¥ Authorized Users", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="ð» Dashboard", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="âï¸ Close", callback_data="close"),
            InlineKeyboardButton(text="ð Go Back", callback_data="okaybhai"),
        ],
    ]
    return f"ð§  **{MUSIC_BOT_NAME} Settings**", buttons


def volmarkup():
    buttons = [
        [
            InlineKeyboardButton(
                text="ð Reset Audio Volume ð", callback_data="HV"
            )
        ],
        [
            InlineKeyboardButton(text="ð Low Vol", callback_data="LV"),
            InlineKeyboardButton(text="ð Medium Vol", callback_data="MV"),
        ],
        [
            InlineKeyboardButton(text="ð High Vol", callback_data="HV"),
            InlineKeyboardButton(text="ð Amplified Vol", callback_data="VAM"),
        ],
        [
            InlineKeyboardButton(
                text="ð½ Custom Volume ð½", callback_data="Custommarkup"
            )
        ],
        [InlineKeyboardButton(text="ð Go back", callback_data="settingm")],
    ]
    return f"ð§  **{MUSIC_BOT_NAME} Settings**", buttons


def custommarkup():
    buttons = [
        [
            InlineKeyboardButton(text="+10", callback_data="PTEN"),
            InlineKeyboardButton(text="-10", callback_data="MTEN"),
        ],
        [
            InlineKeyboardButton(text="+25", callback_data="PTF"),
            InlineKeyboardButton(text="-25", callback_data="MTF"),
        ],
        [
            InlineKeyboardButton(text="+50", callback_data="PFZ"),
            InlineKeyboardButton(text="-50", callback_data="MFZ"),
        ],
        [InlineKeyboardButton(text="ð¼Custom Volume ð¼", callback_data="AV")],
    ]
    return f"ð§  **{MUSIC_BOT_NAME} Settings**", buttons


def usermarkup():
    buttons = [
        [
            InlineKeyboardButton(text="ð¥ Everyone", callback_data="EVE"),
            InlineKeyboardButton(text="ð Admins", callback_data="AMS"),
        ],
        [
            InlineKeyboardButton(
                text="ð Authorized Users Lists", callback_data="USERLIST"
            )
        ],
        [InlineKeyboardButton(text="ð Go back", callback_data="settingm")],
    ]
    return f"ð§  **{MUSIC_BOT_NAME} Settings**", buttons


def dashmarkup():
    buttons = [
        [
            InlineKeyboardButton(text="âï¸ Uptime", callback_data="UPT"),
            InlineKeyboardButton(text="ð¾ Ram", callback_data="RAT"),
        ],
        [
            InlineKeyboardButton(text="ð» Cpu", callback_data="CPT"),
            InlineKeyboardButton(text="ð½ Disk", callback_data="DIT"),
        ],
        [InlineKeyboardButton(text="ð Go back", callback_data="settingm")],
    ]
    return f"ð§  **{MUSIC_BOT_NAME} Settings**", buttons

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

check_button = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text = "Obunani tekshirish!", callback_data="check_subs")
    ]]
)
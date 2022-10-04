from aiogram.types import InlineKeyboardButton, inlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from telegram import InlineKeyboardMarkup


post_callback = CallbackData("create_post", "action")


confirmation_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text = "🆗 Chop etish", callback_data=post_callback.new(action = "post")),
        InlineKeyboardButton(text = "❌ Rad etish", callback_data = post_callback.new(action = "cancel"))
    ]]
)
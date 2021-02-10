from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.menu import mainmenu_markup
from keyboards.inline.menu_keyboards import choise_language_markup, inline_menu_markup
from loader import dp
from utils.db_api.db_commands import choise_lang, add_newuser
from utils.db_api.models import Users
from utils.db_api.text import choise_lang_text, menu_text


@dp.message_handler(commands=["start"])
async def bot_start(message: types.Message):
    if await Users.select('id').where(Users.chat_id == message.from_user.id).gino.scalar():
        lang = await choise_lang(message.from_user.id)
    else:
        await add_newuser(chat_id=message.from_user.id,
                          username=message.from_user.username,
                          full_name=message.from_user.full_name)
        lang = "uk"
    if lang == "ru":
        hi = "Привет"
    else:
        hi = "Вітаю"
    await message.answer(f'{hi}, {message.from_user.full_name}! ',
                         reply_markup=await mainmenu_markup(lang))
    if await Users.select('lang').where(Users.chat_id == message.from_user.id).gino.scalar():
        text = await menu_text()
        markup = await inline_menu_markup(lang)
    else:
        text = await choise_lang_text()
        markup = await choise_language_markup(key=1)
    await message.answer(text=text, reply_markup=markup, parse_mode="HTML")

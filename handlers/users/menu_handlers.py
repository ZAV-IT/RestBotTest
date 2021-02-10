from aiogram import types

from keyboards.inline.menu_keyboards import categories_keyboard, choise_language_markup
from loader import dp
from utils.db_api.db_commands import choise_lang, add_newuser
from utils.db_api.models import MainMenu, Users
from utils.db_api.text import choise_lang_text, categories_text


@dp.message_handler()
async def beggining(message: types.Message):
    chat_id = message.from_user.id
    # Регистрация нового юзера
    if await Users.select('id').where(Users.chat_id == chat_id).gino.scalar():
        pass
    else:
        chat_id = message.from_user.id
        username = message.from_user.username
        full_name = message.from_user.full_name
        await add_newuser(chat_id=chat_id,
                          username=username,
                          full_name=full_name)
        # Перебор текста меню:
    key = 1
    lang = await choise_lang(message.from_user.id)
    for i in (await MainMenu.select(lang).gino.all()):
        # print("MESSAGE = " + str(message.text))
        # print("I = " + str(i[0]))
        # print("KEY = " + str(key))
        if message.text == i[0]:
            if await Users.select('lang').where(Users.chat_id == chat_id).gino.scalar():
                # print("Совпало")
                markup = await categories_keyboard(key=key, lang=lang)
                text = await categories_text(key=key, lang=lang)
            else:
                markup = await choise_language_markup(key=1)
                text = await choise_lang_text()
            await message.answer(text=text, reply_markup=markup)
        key += 1

    #     # Перебор текста меню:
    #     key = 1
    #     lang = await choise_lang(message.from_user.id)
    #     markup = await categories_keyboard(key=key, chat_id=message.from_user.id)
    #     text = await categories_text(key=key, lang=lang)
    #     for i in (await MainMenu.select(lang).gino.all()):
    #         if key == 1:
    #             pass
    #         else:
    #             if message.text == i[0]:
    #                 markup = await categories_keyboard(key=key, chat_id=message.from_user.id)
    #                 text = await categories_text(key=key, lang=lang)
    #                 check = 1
    #         key += 1
    # else:
    #     markup = await choise_language_markup(key=1)
    #     text = await choise_lang_text()
    # await message.answer(text=text, reply_markup=markup)



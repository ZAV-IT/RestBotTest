from aiogram.dispatcher.webhook import EditMessageText, EditMessageReplyMarkup, AnswerCallbackQuery, SendMessage
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.default.menu import mainmenu_markup
from keyboards.inline.callback_datas import callback_menu, callback_lang, move_card, like_button, menu_button
from keyboards.inline.menu_keyboards import markup_card_dishe, inline_menu_markup, categories_keyboard
from loader import dp
from utils.db_api.db_commands import choise_lang
from utils.db_api.models import Dishes, Users
from utils.db_api.text import card_dishe_text, categories_text


@dp.callback_query_handler(menu_button.filter(push="on"))
async def def_menu_button(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=10)
    inline_message_id = call.inline_message_id
    text = "Меню:"
    lang = await choise_lang(call.from_user.id)
    markup = await inline_menu_markup(lang=lang)
    return EditMessageText(
        inline_message_id=inline_message_id,
        text=text,
        reply_markup=markup
    )


@dp.callback_query_handler(like_button.filter())
async def def_like_button(call: CallbackQuery, callback_data: dict):
    button_status = callback_data.get("like_status")
    dishe_id = int(callback_data.get("dishe_id"))
    lang = callback_data.get("lang")
    chat_id = call.from_user.id
    inline_message_id = call.inline_message_id
    username = call.from_user.username
    full_name = call.from_user.full_name
    likes = await Users.select('like').where(Users.chat_id == chat_id).gino.scalar()
    text = ":-)"
    if button_status == "on":
        if likes.count(dishe_id) == 0:
            likes.append(dishe_id)
            if lang == "ru":
                text = "Добавленно в избранное 🥰"
            else:
                text = "Додано до улюбленого 🥰"
    if button_status == "off":
        if likes.count(dishe_id) != 0:
            likes.remove(dishe_id)
            if lang == "ru":
                text = "Удалено из избранного 😞"
            else:
                text = "Видалено з улюбленого 😞"
    await call.answer(text=text,
                      show_alert=True,
                      cache_time=10)
    select = await Users.query.where(Users.chat_id == chat_id).gino.first()
    await select.update(like=likes).apply()

    markup = await markup_card_dishe(
        lang=lang,
        chat_id=chat_id,
        dishe_id=dishe_id
    )
    return EditMessageReplyMarkup(
        inline_message_id=inline_message_id,
        reply_markup=markup
    )


@dp.callback_query_handler(move_card.filter())
async def def_move_card(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=10)
    direction = callback_data.get("card_direction")
    dishe_id = int(callback_data.get("dishe_id"))
    lang = callback_data.get("lang")
    chat_id = call.from_user.id
    inline_message_id = call.inline_message_id
    category = await Dishes.select('category_id').where(Dishes.name_id == dishe_id).gino.scalar()
    categories = await Dishes.select('name_id').where(Dishes.category_id == category).gino.all()
    list_categ = []
    for i in categories:
        list_categ.append(int(i[0]))
    print(list_categ)
    print(list_categ.index(dishe_id))
    if len(list_categ) > 1:
        if direction == "prev":
            if int(dishe_id) == int(list_categ[0]):
                dishe_id = int(list_categ[-1])
            else:
                dishe_id -= 1
        else:
            if int(dishe_id) == int(list_categ[-1]):
                dishe_id = int(list_categ[0])
            else:
                dishe_id += 1
    text = await card_dishe_text(lang=lang,
                                 dishe_id=dishe_id)
    markup = await markup_card_dishe(
        lang=lang,
        chat_id=chat_id,
        dishe_id=dishe_id
    )
    return EditMessageText(
        inline_message_id=inline_message_id,
        text=text,
        reply_markup=markup
    )


@dp.callback_query_handler(callback_lang.filter())
async def call_choice_lang(call: CallbackQuery, callback_data: dict):
    print(call)
    await call.answer(cache_time=10)
    lang = callback_data.get("index_lang")
    chat_id = call.from_user.id
    select = await Users.query.where(Users.chat_id == chat_id).gino.first()
    await select.update(lang=lang).apply()
    key = int(callback_data.get("key"))
    if lang == "ru":
        text = "Вы выбрали русский язык 🇷🇺"
        button_text = "Нажмите, что бы вернуться."
    else:
        text = "Вы обрали українську мову 🇺🇦"
        button_text = "Натисніть, щоб повернутися."
    if int(key) == 0:
        inline_message_id = call.inline_message_id
        inline_text = callback_data.get("inline_text")
        if inline_text == "-":
            inline_text = " "
        markup = InlineKeyboardMarkup(row_width=1)
        markup.insert(InlineKeyboardButton(
            text=button_text,
            switch_inline_query_current_chat=inline_text
        ))
        return EditMessageText(
            inline_message_id=inline_message_id,
            text=text,
            reply_markup=markup
        )
    else:
        markup = await mainmenu_markup(lang)
        await call.message.answer(
            text=text,
            reply_markup=markup,
            parse_mode="HTML"
        )
        markup = await categories_keyboard(key=key, lang=lang)
        text = await categories_text(key=key, lang=lang)
        await call.message.answer(
            text=text,
            reply_markup=markup,
            parse_mode="HTML"
        )

        # return SendMessage(
        #     chat_id=chat_id,
        #     text=text_2,
        #     reply_markup=markup_2,
        #     parse_mode="HTML"
        # )

        # message_id = call.message.message_id

        # return await call.message.answer(text=text, reply_markup=markup)
        #
        # return EditMessageText(
        #     chat_id=chat_id,
        #     message_id=message_id,
        #     text=text,
        #     reply_markup=markup
        # )

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_datas import make_callback_menu, make_callback_lang, make_move_card, make_like_button, \
    menu_button
from utils.db_api.db_commands import get_categories, choise_lang, add_newuser
from utils.db_api.models import Users, ChoiseLang, Dishes
import json


async def markup_card_dishe(lang,
                            chat_id,
                            dishe_id):
    ingredients = json.loads(await Dishes.select('ingredients').where(Dishes.name_id == dishe_id).gino.scalar())[
        "ingredients"]
    string_ingredients = "No"
    ingr_name = "name_" + lang
    for key in ingredients:
        if key[ingr_name] == '-':
            pass
        else:
            string_ingredients = "Yes"
    price = await Dishes.select('price').where(Dishes.name_id == dishe_id).gino.scalar()
    text_basket = await Users.select('summa').where(Users.chat_id == chat_id).gino.scalar()

    # Работа с JSON:
    # purchase = json.loads(await Users.select('choice').where(Users.chat_id == chat_id).gino.scalar())
    # for key2 in purchase.keys():
    #     if int(key2) != 0:
    #         value = purchase[key2]
    #         text_basket += int(value["price"]) * int(value["quantity"])
    #         for key3 in value["ingredients"]:
    #             if key3[ingr_name] != '-':
    #                 text_basket += int(key3["price"])

    if lang == "ru":
        text_buy = "Приобрести"
        text_ingredients = "Редактировать ингредиенты"
        text_menu = " Меню"
    else:
        text_buy = "Придбати"
        text_ingredients = "Редагувати інгридієнти"
        text_menu = " Меню"

    likes = await Users.select('like').where(Users.chat_id == chat_id).gino.scalar()
    if likes.count(dishe_id) == 0:
        text_like = "🤍"
        button_like = make_like_button(dishe_id=int(dishe_id),
                                       like_status="on",
                                       lang=lang)
    else:
        text_like = "❤️"
        button_like = make_like_button(dishe_id=int(dishe_id),
                                       like_status="off",
                                       lang=lang)
    button_buy = "Empty"
    button_basket = "Empty"
    button_ingredients = "Empty"
    button_forward = make_move_card(dishe_id=int(dishe_id),
                                    card_direction="next",
                                    lang=lang)
    button_menu = menu_button.new(push="on")
    button_backward = make_move_card(dishe_id=int(dishe_id),
                                     card_direction="prev",
                                     lang=lang)
    text_menu = f"📜  {text_menu}"
    text_ingredients = f"📝 {text_ingredients}"
    text_buy = f"{price}₴ {text_buy}"
    text_basket = f"🛒   {text_basket}₴"
    if string_ingredients == "Yes":
        inline_keyboard = [
            [
                InlineKeyboardButton(text=text_buy, callback_data=button_buy, parce_mode="HTML")
            ],
            [
                InlineKeyboardButton(text=text_like, callback_data=button_like),
                InlineKeyboardButton(text=text_basket, callback_data=button_basket)

            ],
            [
                InlineKeyboardButton(text=text_ingredients, callback_data=button_ingredients)
            ],
            [
                InlineKeyboardButton(text="<<<", callback_data=button_backward),
                InlineKeyboardButton(text=text_menu, callback_data=button_menu),
                InlineKeyboardButton(text=">>>", callback_data=button_forward),
            ]
        ]
    else:
        inline_keyboard = [
            [
                InlineKeyboardButton(text=text_buy, callback_data=button_buy, parce_mode="HTML")
            ],
            [
                InlineKeyboardButton(text=text_like, callback_data=button_like),
                InlineKeyboardButton(text=text_basket, callback_data=button_basket)

            ],
            [
                InlineKeyboardButton(text="<<<", callback_data=button_backward),
                InlineKeyboardButton(text=text_menu, callback_data=button_menu),
                InlineKeyboardButton(text=">>>", callback_data=button_forward),
            ]
        ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


async def choise_language_markup(key,
                                 inline_text=' '):
    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup(row_width=1)
    for i in await ChoiseLang.select("choice_lang", "index_lang").gino.all():
        markup.insert(InlineKeyboardButton(
            text=i[0],
            callback_data=make_callback_lang(lang=i[1],
                                             key=key,
                                             inline_text=inline_text)
        ))
    return markup


async def inline_menu_markup(lang):
    markup = InlineKeyboardMarkup(row_width=2)
    # Забираем список товаров из базы данных с РАЗНЫМИ категориями и проходим по нему
    categories = await get_categories(lang=lang)
    categories.reverse()
    for category in categories:
        if lang == "ru":
            button_text = f"{category.category_name_ru}"
        else:
            button_text = f"{category.category_name_uk}"
        query_text = f"{category.category_code}"
        markup.insert(InlineKeyboardButton(
            text=button_text,
            switch_inline_query_current_chat=query_text
        ))
    return markup


# Создаем функцию, которая отдает клавиатуру с доступными категориями
async def categories_keyboard(key, lang):
    if key == 8:
        markup = await choise_language_markup(key=1)
        return markup
    if key == 1:
        markup = await inline_menu_markup(lang=lang)
        return markup
    if key == 2:
        markup = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Придбати", callback_data="1")
            ],
            [
                InlineKeyboardButton(text="Избранное", callback_data="4"),
                InlineKeyboardButton(text="Корзина", callback_data="2")

            ],
            [
                InlineKeyboardButton(text="Редактировать ингридиенты", callback_data="6")
            ],
            [
                InlineKeyboardButton(text="<<<", callback_data="3"),
                InlineKeyboardButton(text="Назад", callback_data="7"),
                InlineKeyboardButton(text=">>>", callback_data="5"),
            ]
        ])
        return markup

    if key == 3:
        callback_data = "Empy"

        markup = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Скоро будет", callback_data=callback_data)
            ]
        ])
        return markup

    if key == 4:
        callback_data = "Empty"
        markup = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text=f"Key = {key}", callback_data=callback_data)
            ]
        ])
        return markup

    if key == 5:
        callback_data = "Empty"
        markup = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text=f"Key = {key}", callback_data=callback_data)
            ]
        ])
        return markup

    if key == 6:
        callback_data = "Empty"
        markup = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text=f"Key = {key}", callback_data=callback_data)
            ]
        ])
        return markup

    if key == 7:
        callback_data = "Empty"
        markup = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text=f"Key = {key}", callback_data=callback_data)
            ]
        ])
        return markup

from aiogram.utils.callback_data import CallbackData

menu_button = CallbackData("menu",
                           "push")

like_button = CallbackData("liked",
                           "like_status",
                           "dishe_id",
                           "lang")

move_card = CallbackData("move_card",
                         "card_direction",
                         "dishe_id",
                         "lang")

callback_menu = CallbackData("call_menu",
                             "chat_id",
                             "lang",
                             "key",
                             "level",
                             "category",
                             "subcategory",
                             "item_id")

callback_lang = CallbackData("langv_menu",
                             "index_lang",
                             "key",
                             "inline_text")


def make_callback_lang(lang, key, inline_text='-'):
    if inline_text:
        pass
    else:
        inline_text = "-"
    menu = callback_lang.new(index_lang=lang,
                             key=key,
                             inline_text=inline_text)
    return menu


def make_like_button(dishe_id,
                     like_status,
                     lang="uk"):
    menu = like_button.new(dishe_id=dishe_id,
                           like_status=like_status,
                           lang=lang)
    return menu


def make_move_card(dishe_id,
                   card_direction,
                   lang="uk"):
    menu = move_card.new(dishe_id=dishe_id,
                         card_direction=card_direction,
                         lang=lang)
    return menu


def make_callback_menu(chat_id,
                       lang="uk",
                       key=1,
                       level=1,
                       category="0",
                       subcategory="0",
                       item_id="0"):
    menu = callback_menu.new(chat_id=chat_id,
                             lang=lang,
                             key=key,
                             level=level,
                             category=category,
                             subcategory=subcategory,
                             item_id=item_id)
    return menu

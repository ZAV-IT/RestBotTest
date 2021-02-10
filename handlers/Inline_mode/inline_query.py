from aiogram.dispatcher.webhook import AnswerInlineQuery
from aiogram.types import InlineQueryResultArticle, InlineQuery, InputTextMessageContent

from keyboards.inline.menu_keyboards import markup_card_dishe, choise_language_markup
from loader import dp
from utils.db_api.db_commands import choise_lang, add_newuser
from utils.db_api.models import Dishes, Users
from utils.db_api.text import card_dishe_text, choise_lang_text


@dp.inline_handler()
async def inline_mode(call: InlineQuery):
    chat_id = call.from_user.id
    if await Users.select('id').where(Users.chat_id == chat_id).gino.scalar():
        text = call.query.lower()
        lang = await choise_lang(chat_id)
        col_name = "name_" + lang
        specification_name = "specification_" + lang
        result = []
        # Проверка ввода категорий
        categories = await Dishes.query.distinct(Dishes.category_code).gino.all()
        for category in categories:
            category_code = f"{category.category_code}"
            if text == category_code:
                values = (await Dishes.select("category_symbol",
                                              specification_name,
                                              "photo",
                                              "price",
                                              "weight",
                                              "name_id",
                                              "symbol_dishe",
                                              "symbol_dishe_2",
                                              "symbol_dishe_3",
                                              col_name).where(Dishes.category_code == category_code).gino.all()
                          )
                for value in values:
                    result.append(await inline_query_article(value=value,
                                                             chat_id=chat_id,
                                                             inline_text=text))
        if not result:
            # Выбор общих значений по поиску блюд
            for i_1 in await Dishes.select("id").gino.all():
                i_1 = i_1[0]
                value = (await Dishes.select("category_symbol",
                                             specification_name,
                                             "photo",
                                             "price",
                                             "weight",
                                             "name_id",
                                             "symbol_dishe",
                                             "symbol_dishe_2",
                                             "symbol_dishe_3",
                                             col_name,
                                             "name_uk",
                                             "name_ru").where(
                    Dishes.id == i_1
                ).gino.all())[0]
                if ((value[9]).lower()).count(text) or ((value[10]).lower()).count(text) != 0:
                    result.append(await inline_query_article(value=value,
                                                             chat_id=chat_id,
                                                             inline_text=text))
        if not result:
            result.append(InlineQueryResultArticle(id="999999",
                                                   title="Ничего нет",
                                                   description="Совсем ничего",
                                                   input_message_content=
                                                   InputTextMessageContent(message_text="Бабабабаба")))
        return AnswerInlineQuery(call.id, results=result, cache_time=10)
    else:
        username = call.from_user.username
        full_name = call.from_user.full_name
        await add_newuser(chat_id=chat_id,
                          username=username,
                          full_name=full_name)


##############

async def inline_query_article(value, chat_id, inline_text):
    category_symbol = value[0]
    specification = value[1]
    photo = value[2]
    price = value[3]
    weight = value[4]
    result_id = value[5]
    symbol_dishe = value[6]
    symbol_dishe_2 = value[7]
    symbol_dishe_3 = value[8]
    name = value[9]
    if specification == "-":
        specification = ""
    if symbol_dishe == "-":
        symbol_dishe = ""
    if symbol_dishe_2 == "-":
        symbol_dishe_2 = ""
    if symbol_dishe_3 == "-":
        symbol_dishe_3 = ""
    title_text = f"{symbol_dishe}{symbol_dishe_2}{symbol_dishe_3}{name}"
    description_text = f"{category_symbol} {str(price)}₴ {str(specification)} ⚖:{str(weight)}г."
    if await Users.select('lang').where(Users.chat_id == chat_id).gino.scalar():
        lang = await Users.select('lang').where(Users.chat_id == chat_id).gino.scalar()
        message_text = await card_dishe_text(dishe_id=result_id,
                                             lang=lang)
        markup = await markup_card_dishe(chat_id=chat_id,
                                         dishe_id=result_id,
                                         lang=lang)
    else:
        message_text = await choise_lang_text()
        markup = await choise_language_markup(key=0,
                                              inline_text=inline_text)

    text = InputTextMessageContent(message_text=message_text,
                                   parse_mode="HTML",
                                   disable_web_page_preview=False)
    result = InlineQueryResultArticle(id=str(result_id),
                                      title=title_text,
                                      description=description_text,
                                      input_message_content=text,
                                      thumb_url=photo,
                                      reply_markup=markup)
    return result

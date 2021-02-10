from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from utils.db_api.models import MainMenu


async def mainmenu_markup(lang="uk"):
    markup = ReplyKeyboardMarkup(
        row_width=2,
        resize_keyboard=True)
    for i in await MainMenu.select(lang).gino.all():
        markup.insert(KeyboardButton(text=i[0]))
    print((await MainMenu.select(lang).gino.all())[1][0])
    return markup

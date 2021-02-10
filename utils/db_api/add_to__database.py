from data.config import DATABASE
from utils.db_api.db_commands import add_item, add_mainmenu, add_choiseln

import asyncio

from utils.db_api.database import create_db

# Используем эту функцию, чтобы заполнить базу данных товарами
from utils.db_api.dishes import add_dishe
from utils.db_api.models import MainMenu, ChoiseLang


async def add_mainmenus():
    list_temp = [(1, '📖 Меню', '📖 Меню'),
                 (2, '😏 Мій заказ', '😏 Мой заказ'),
                 (3, '🎁 Акції', '🎁 Акции'),
                 (4, '😍 Улюблене', '😍 Избранное'),
                 (5, '⏰ Час роботи', '⏰ Время работы'),
                 (6, '☎️ Контакти', '☎️ Контакты'),
                 (7, '📝 Про ресторан', '📝 О ресторане'),
                 (8, '🇺🇦/🇷🇺 Змінити мову', '🇷🇺/🇺🇦 Сменить язык')]
    for i in list_temp[:]:
        print("ключ: " + str(i[0]))
        if (await MainMenu.select('id').where(MainMenu.id == i[0]).gino.scalar()) == i[0]:
            print("Походу есть")
            # print(await MainMenu.select('id').where(MainMenu.id == i[0]).gino.scalar())
        else:
            print("Добавляю")
            await add_mainmenu(id=i[0],
                               uk=i[1],
                               ru=i[2])


async def add_choiselang():
    list_temp = [(1, 'Обрати українську мову 🇺🇦', 'uk'),
                 (2, 'Выбрать русский язык 🇷🇺', 'ru')]
    for i in list_temp[:]:
        if (await ChoiseLang.select('id').where(ChoiseLang.id == i[0]).gino.scalar()) == i[0]:
            pass
        else:
            await add_choiseln(id=i[0],
                               choice_lang=i[1],
                               index_lang=i[2])


def start_bd():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_db())
    loop.run_until_complete(add_mainmenus())
    loop.run_until_complete(add_choiselang())
    loop.run_until_complete(add_dishe())
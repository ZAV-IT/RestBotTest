from typing import List

from sqlalchemy import and_

from utils.db_api.models import Item, MainMenu, ChoiseLang, Users, Dishes
from utils.db_api.database import db


# Функция для создания нового товара в базе данных. Принимает все возможные аргументы, прописанные в Item
async def add_item(**kwargs):
    new_item = await Item(**kwargs).create()
    return new_item


# Функция для вывода товаров с РАЗНЫМИ категориями
async def get_categories(lang) -> List[Dishes]:
    # category_name = ("category_name_" + lang)
    if lang == "ru":
        value = await Dishes.query.distinct(Dishes.category_name_ru).gino.all()
    else:
        value = await Dishes.query.distinct(Dishes.category_name_uk).gino.all()
    return value


async def get_categories_code(lang) -> List[Dishes]:
    # category_name = ("category_name_" + lang)
    if lang == "ru":
        value = await Dishes.query.distinct(Dishes.category_name_ru).gino.all()
    else:
        value = await Dishes.query.distinct(Dishes.category_name_uk).gino.all()
    return value


# Функция для вывода товаров с РАЗНЫМИ подкатегориями в выбранной категории
async def get_subcategories(category) -> List[Item]:
    return await Item.query.distinct(Item.subcategory_name).where(Item.category_code == category).gino.all()


# Функция для подсчета товаров с выбранными категориями и подкатегориями
async def count_items(category_code, subcategory_code=None):
    # Прописываем условия для вывода (категория товара равняется выбранной категории)
    conditions = [Item.category_code == category_code]

    # Если передали подкатегорию, то добавляем ее в условие
    if subcategory_code:
        conditions.append(Item.subcategory_code == subcategory_code)

    # Функция подсчета товаров с указанными условиями
    total = await db.select([db.func.count()]).where(
        and_(*conditions)
    ).gino.scalar()
    return total


# Функция вывода всех товаров, которые есть в переданных категории и подкатегории
async def get_items(category_code, subcategory_code) -> List[Item]:
    item = await Item.query.where(
        and_(Item.category_code == category_code,
             Item.subcategory_code == subcategory_code)
    ).gino.all()
    return item


# Функция для получения объекта товара по его айди
async def get_item(item_id) -> Item:
    item = await Item.query.where(Item.id == item_id).gino.first()
    return item


# Функция для создания нового значения главного меню в базе данных.
# Принимает все возможные аргументы, прописанные в MainMenu


async def add_newuser(chat_id,
                      username,
                      full_name):
    like = [0, ]
    choice = '{' \
             '"0": {' \
             '"index": 0, ' \
             '"name_uk": "-", ' \
             '"name_ru": "-", ' \
             '"price": 0, ' \
             '"quantity": 0, ' \
             '"weight": 0, ' \
             '"ingredients": [{' \
             '"name_uk": "-", ' \
             '"name_ru": "-", ' \
             '"price": 0, ' \
             '"quantity": 0, ' \
             '"weight": 0}]' \
             '},' \
             '"1": {' \
             '"index": 0, ' \
             '"name_uk": "Гарбузовий крем-суп з чипсами з хамону", ' \
             '"name_ru": "Тыквенный крем-суп с чипсами из хамона", ' \
             '"price": 160, ' \
             '"quantity": 2, ' \
             '"weight": 220, ' \
             '"ingredients": [' \
             '{"name_uk": "Вершки", ' \
             '"name_ru": "Сливки", ' \
             '"price": 10, ' \
             '"quantity": 1, ' \
             '"weight": 5},' \
             '{"name_uk": "Шпинат", ' \
             '"name_ru": "Шпинат", ' \
             '"price": 15, ' \
             '"quantity": 1, ' \
             '"weight": 10}' \
             ']' \
             '}' \
             '}'
    summa = 0
    await newuser_in_db(
        chat_id=chat_id,
        username=username,
        full_name=full_name,
        choice=choice,
        like=like,
        summa=summa
    )
    return newuser_in_db


async def newuser_in_db(**kwargs):
    result = await Users(**kwargs).create()
    return result


async def add_choiseln(**kwargs):
    add_choiseln = await ChoiseLang(**kwargs).create()
    return add_choiseln


async def add_mainmenu(**kwargs):
    new_mainmenu = await MainMenu(**kwargs).create()
    return new_mainmenu


async def add_dishes(**kwargs):
    new_dishes = await Dishes(**kwargs).create()
    return new_dishes


async def choise_lang(chat_id):
    if await Users.select('lang').where(Users.chat_id == chat_id).gino.scalar():
        lang = await Users.select('lang').where(Users.chat_id == chat_id).gino.scalar()
    else:
        lang = "uk"
    return lang


# Функция выбора значений основного меню
async def MainMenuButton(lang='uk'):
    text = (await MainMenu.select(lang).gino.all())[1][0]
    # input(text)
    return text


async def change_lang(chat_id, lang):
    if await Users.select('lang').where(Users.chat_id == chat_id).gino.scalar() == lang:
        pass
    else:
        await Users.update(lang=lang).where(Users.chat_id == chat_id).apply()

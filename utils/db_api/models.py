from sqlalchemy import (Column, Integer, String, Sequence, JSON, ARRAY)
from sqlalchemy import sql
from utils.db_api.database import db


# Создаем класс таблицы клиентов
class Users(db.Model):
    __tablename__ = 'users'
    query: sql.Select

    # Уникальный идентификатор клиента
    id = Column(Integer, Sequence('users_pk'), primary_key=True)

    # Идентификатор клиента в телеграмм
    chat_id = Column(Integer)

    # Выбор языка
    lang = Column(String(2))

    # Код категории (для отображения в колбек дате)
    username = Column(String(20))

    # Название категории (для отображения в кнопке)
    full_name = Column(String(50))

    summa = Column(Integer)

    like = Column(ARRAY(Integer))

    # Код подкатегории (для отображения в колбек дате)
    choice = Column(JSON)



# Создаем класс таблицы главного меню
class MainMenu(db.Model):
    __tablename__ = 'mainmenu'
    query: sql.Select

    # Уникальный идентификатор языка
    id = Column(Integer)

    # Украинский язык
    uk = Column(String(20))

    # Русский язык
    ru = Column(String(20))


class ChoiseLang(db.Model):
    __tablename__ = 'choiselang'
    guery: sql.Select

    # Уникальный идентификатор языка
    id = Column(Integer)
    choice_lang = Column(String(50))
    index_lang = Column(String(5))


class Dishes(db.Model):
    __tablename__ = 'dishes'
    query: sql.Select

    # Уникальный идентификатор товара
    id = Column(Integer, primary_key=True)

    # Уникальный идентификатор товара
    category_id = Column(Integer)

    # Код категории (для отображения в колбек дате)
    category_code = Column(String(20))

    # Код категории (для отображения в колбек дате)
    category_symbol = Column(String(10))

    # Название категории (для отображения в кнопке)
    category_name_uk = Column(String(50))

    # Название категории (для отображения в кнопке)
    category_name_ru = Column(String(50))

    # Название, фото и цена блюда
    name_id = Column(Integer)

    name_uk = Column(String(50))
    name_ru = Column(String(50))
    photo = Column(String(250))

    price = Column(Integer)

    # Вес блюда
    weight = Column(Integer)

    # Описание блюда
    specification_uk = Column(String(250))
    specification_ru = Column(String(250))

    # Ингридиенты
    ingredients = Column(JSON)

    # Спец.символы блюда
    symbol_dishe = Column(String(10))
    symbol_dishe_name_uk = Column(String(30))
    symbol_dishe_name_ru = Column(String(30))
    symbol_dishe_2 = Column(String(10))
    symbol_dishe_name_2_uk = Column(String(30))
    symbol_dishe_name_2_ru = Column(String(30))
    symbol_dishe_3 = Column(String(10))
    symbol_dishe_name_3_uk = Column(String(30))
    symbol_dishe_name_3_ru = Column(String(30))


# Создаем класс таблицы товаров
class Item(db.Model):
    __tablename__ = 'items'
    query: sql.Select

    # Уникальный идентификатор товара
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)

    # Код категории (для отображения в колбек дате)
    category_code = Column(String(20))

    # Название категории (для отображения в кнопке)
    category_name = Column(String(50))

    # Код подкатегории (для отображения в колбек дате)
    subcategory_code = Column(String(50))

    # Название подкатегории (для отображения в кнопке)
    subcategory_name = Column(String(20))

    # Название, фото и цена товара
    name = Column(String(50))
    photo = Column(String(250))
    price = Column(Integer)

    def __repr__(self):
        return f"""
Товар № {self.id} - "{self.name}"
Цена: {self.price}"""

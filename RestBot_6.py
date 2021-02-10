# Привязка SQL либов

import mysql.connector
from mysql.connector import Error

# Привязка телеграмм либов

import telebot
from telebot import types

# Привязка документа и значений оттуда

import RestToken
bot = telebot.TeleBot(RestToken.BotToken)
idchatbot = (RestToken.TeleBotId)
sqlhost = (RestToken.SQL_Serv)
sqluser = (RestToken.SQL_User)
sqlpsswd = (RestToken.SQL_Psswd)
sqlbd = (RestToken.SQL_BD)

# Функция коннекта к серверу MySQL

def create_server_connection(host_name, user_name, user_password):
	main_connection = None
	try:
		main_connection = mysql.connector.connect(
			host = host_name,
			user = user_name,
			passwd = user_password
		)
		print ("Connection to MySQL BD susseful")
	except Error as e:
		print (f"The error '{e}' occurred.")

	return main_connection

# Функция создания базы данных

input(create_server_connection(sqlhost, sqluser, sqlpsswd))

def create_database(main_connection = create_server_connection(sqlhost, sqluser, sqlpsswd), query = ("CREATE DATABASE IF NOT EXISTS " + sqlbd)):
    cursor = main_connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

# Создание базы данных

input(sqlbd)

create_database()

# Функция коннекта к базе данных

def create_connection(host_name, user_name, user_password, db_name):
	connection = None
	try:
		connection = mysql.connector.connect(
			host = host_name,
			user = user_name,
			passwd = user_password,
			database = db_name
		)
		print ("Connection to MySQL BD susseful")
	except Error as e:
		print (f"The error '{e}' occurred.")

	return connection
	
connection = create_connection(sqlhost, sqluser, sqlpsswd, sqlbd)

# Функция выполнения запросов
		
def execute_query(connection, query):
     cursor = connection.cursor()
     try:
         cursor.execute(query)
         connection.commit()
         print("Query executed successfully")
     except Error as e:
         print(f"The error '{e}' occurred")

# Создание таблицы language

create_language_table = """
CREATE TABLE IF NOT EXISTS language (
  id INT, 
  lang TEXT
) ENGINE = InnoDB
"""

execute_query(connection, create_language_table)

# Создание таблицы mainmenu

create_mainmenu_table = """
CREATE TABLE IF NOT EXISTS mainmenu (
  id INT,
  ua TEXT,
  ru TEXT
) ENGINE = InnoDB
"""

execute_query(connection, create_mainmenu_table)

# Создание таблицы categorymenu

create_categorymenu_table = """
CREATE TABLE IF NOT EXISTS categorymenu (
  id INT, 
  ua TEXT,
  ru TEXT
) ENGINE = InnoDB
"""

execute_query(connection, create_categorymenu_table)

# Функция чтения таблиц

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
	
#Заполнение language

print ("\nЗаполнение таблицы Языки:\n")

list_temp = [(1 , 'Залишити українську 🇺🇦'),
	(2, 'Выбрать русский язык 🇷🇺')]
	
for i in list_temp[:]:
	print ("ключ: " + str(i[0]))
	try:
		if (execute_read_query(connection, "SELECT * FROM language WHERE id = " + str(i[0])))[0][0] != i[0]:
			print ("   Значения еще нет, добавляю:")
			create_values = ("INSERT INTO `language` (`id`, `lang`) VALUES " + str(i))
			execute_query(connection, create_values)			
		else:
			print ("Вродь уже есть..")
			print ("Данные таблицы:  " + str(execute_read_query(connection, "SELECT * FROM language WHERE id = " + str(i[0]))[0][0]))
	except IndexError:
		create_values = ("INSERT INTO `language` (`id`, `lang`) VALUES " + str(i))
		execute_query(connection, create_values)	

# Заполнение данными main_menu

print ("\nЗаполнение таблицы Основное меню\n")

list_temp = [(1 , '📖 Меню', '📖 Меню'),
	(2, '😏 Мій заказ', '😏 Мой заказ'),
	(3, '🎁 Акції', '🎁 Акции'),
	(4, '😍 Улюблене', '😍 Избранное'),
	(5, '⏰ Час роботи', '⏰ Время работы'),
	(6, '☎️ Контакти', '☎️ Контакты'),
	(7, '📝 Про ресторан', '📝 О ресторане'),
	(8, '🇺🇦/🇷🇺 Змінити мову', '🇷🇺/🇺🇦 Сменить язык')]
	
for i in list_temp[:]:
	print ("ключ: " + str(i[0]))
	try:
		if (execute_read_query(connection, "SELECT * FROM mainmenu WHERE id = " + str(i[0])))[0][0] != i[0]:
			print ("   Значения еще нет, добавляю:")
			create_values = ("INSERT INTO `mainmenu` (`id`, `ua`, `ru`) VALUES ( " + i)
			execute_query(connection, create_values)			
		else:
			print ("Вродь уже есть..")
			print ("Данные таблицы:  " + str(execute_read_query(connection, "SELECT * FROM mainmenu WHERE id = " + str(i[0]))[0][0]))
	except IndexError:
		create_values = ("INSERT INTO `mainmenu` (`id`, `ua`, `ru`) VALUES " + str(i))
		execute_query(connection, create_values)

# Чтение таблицы USERS
print ("\nТаблица Языки:\n")

resvalues = execute_read_query(connection, "SELECT * FROM language")

for resname in resvalues:
	print (resname)

print ("\nТаблица Главное Меню:\n")

resvalues = execute_read_query(connection, "SELECT * FROM mainmenu")

for resname in resvalues:
	print (resname)
	
# Глобальные индексы

global key_index
global lang
global key_old
#global daydescr
#global datedescr
#global resjob
#global jobuuid
key_index = 0
lang = 2
key_old = 1

print("Проверка:\n")
print(str(execute_read_query(connection, "SELECT * FROM language")[0][1]))
print(str(execute_read_query(connection, "SELECT * FROM language")[1][1]))

print ("бот ок")

#Функция главной клавиатуры

def main_keyboard(userlang):
	mainmarkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton(execute_read_query(connection, "SELECT * FROM mainmenu")[0][userlang])
	item2 = types.KeyboardButton(execute_read_query(connection, "SELECT * FROM mainmenu")[1][userlang])
	item3 = types.KeyboardButton(execute_read_query(connection, "SELECT * FROM mainmenu")[2][userlang])
	item4 = types.KeyboardButton(execute_read_query(connection, "SELECT * FROM mainmenu")[3][userlang])
	item5 = types.KeyboardButton(execute_read_query(connection, "SELECT * FROM mainmenu")[4][userlang])
	item6 = types.KeyboardButton(execute_read_query(connection, "SELECT * FROM mainmenu")[5][userlang])
	item7 = types.KeyboardButton(execute_read_query(connection, "SELECT * FROM mainmenu")[6][userlang])
	item8 = types.KeyboardButton(execute_read_query(connection, "SELECT * FROM mainmenu")[7][userlang])
	mainmarkup.add(item1, item2)
	mainmarkup.add(item3, item4)
	mainmarkup.add(item5, item6)
	mainmarkup.add(item7, item8)
	return mainmarkup

# Меню основное телеграмма
	
@bot.message_handler(commands=['start'])
def welcome(message):

	bot.send_message(message.chat.id, "Вітаю, {0.first_name}!\n".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup = main_keyboard(1))

# Клавиатура выбора языка	
	
	markup = telebot.types.InlineKeyboardMarkup()
	markup.add(telebot.types.InlineKeyboardButton(text=(execute_read_query(connection, "SELECT * FROM language")[0][1]), callback_data="ua_lang"))
	markup.add(telebot.types.InlineKeyboardButton(text=(execute_read_query(connection, "SELECT * FROM language")[1][1]), callback_data="ru_lang"))
	bot.send_message(idchatbot, text="Оберіть мову / Выберите язык:", reply_markup=markup)

# Убирание клавиатуры

@bot.message_handler(commands=['deletekeyboard'])
def start_message(message):
	bot.send_message(message.chat.id, "Клавиатура убрана", reply_markup = types.ReplyKeyboardRemove())
#	bot.send_message(message.chat.id, text="Клавиатура удалена", reply_markup=types.ReplyKeyboardRemove())

# Обработчик инлайн клавиатуры

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.data == "ua_lang":
			bot.send_message(call.message.chat.id, "Остаемся на украинском")
		elif call.data == "ru_lang":
			bot.send_message(call.message.chat.id, "Переходим на русский")
		
#		bot.edit_message_text(chat_id = call.message.chat.id, 
#		  text = "Тыц",
#  		  reply_markup = None
#		 )
	except Exception as e:
		print (repr(e))




	
if __name__ == "__main__":
    bot.polling(none_stop=True)
		
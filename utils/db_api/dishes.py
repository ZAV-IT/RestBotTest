from utils.db_api.db_commands import add_dishes
from utils.db_api.models import Dishes

ssymbol_dict_uk = {
    "🆕": "Новинка",
    "🧒": "Дитяча страва",
    "🌶": "Гостра страва",
    "🌰": "Страви з додаванням горіхів",
    "🦐": "Страва з морепродуктами",
    "🐚": "Страва з додаванням часнику",
    "-": "-"
}

ssymbol_dict_ru = {
    "🆕": "Новинка",
    "🧒": "Детское блюдо",
    "🌶": "Острое блюдо",
    "🌰": "Блюдо с добавлением орехов",
    "🦐": "Блюдо с морепродуктами",
    "🐚": "Блюдо с добавлением орехов",
    "-": "-"
}

list_categories = [
    ('1', 'soups', '🍲 ', '🍲 Супи', '🍲 Супы'),
    # 1
    ('2', 'breakfasts', '🍳 ', '🍳Сніданки', '🍳Завтраки'),
    # 2
    ('3', 'salads', '🥗 ', '🥗 Салати та закуски', '🥗 Салаты и закуски'),
    # 3
    ('4', 'bruschets', '🥙', '🥙 Брускети', '🥙 Брускеты'),
    # 4
    ('5', 'main_dishes', '🍽 ', '🍽 Основні страви', '🍽 Основные блюда'),
    # 5
    ('6', 'deserts', '🧁 ', '🧁 Десерти в асортіменті', '🧁 Десерты в асоменте'),
    # 6
    ('7', 'coffee', '🍵 ', '🍵 Кава', '🍵 Кофе'),
    # 7
    ('8', 'hand_coffee', '☕ ', '☕️ Кава ручного заварювання', '☕️ Кофе ручного заваривания'),
    # 8
    ('9', 'drinks', '🥛 ', '🥛 Безалкогольні напої', '🥛 Безалкогольные напитки')
]


def value_string(num_category,
                 list_categories=list_categories,
                 ssymbol_dict_uk=ssymbol_dict_uk,
                 ssymbol_dict_ru=ssymbol_dict_ru,
                 name_id=0,
                 name_uk='-',
                 name_ru='-',
                 photo='https://wcs.strans.ua/media/photo/tecdoc/tecdoc_photo/photostrans/origin/531271%20_.jpg?',
                 price='0',
                 weight='0',
                 specification_uk='-',
                 specification_ru='-',
                 ingredients='{"ingredients": [{"name_uk": "-", "name_ru": "-",'
                             '"price": "0", "quantity": "0", "weight": "0"}]}',
                 symbol_dishe='-',
                 symbol_dishe_2='-',
                 symbol_dishe_3='-'):
    symbol_dishe_name_uk = ssymbol_dict_uk.get(symbol_dishe)
    symbol_dishe_name_ru = ssymbol_dict_ru.get(symbol_dishe)
    symbol_dishe_name_2_uk = ssymbol_dict_uk.get(symbol_dishe_2)
    symbol_dishe_name_2_ru = ssymbol_dict_ru.get(symbol_dishe_2)
    symbol_dishe_name_3_uk = ssymbol_dict_uk.get(symbol_dishe_3)
    symbol_dishe_name_3_ru = ssymbol_dict_ru.get(symbol_dishe_3)
    list_1 = (list_categories[(num_category - 1)])
    list_2 = (name_id,
              name_uk,
              name_ru,
              photo,
              price,
              weight,
              specification_uk,
              specification_ru,
              ingredients,
              symbol_dishe,
              symbol_dishe_name_uk,
              symbol_dishe_name_ru,
              symbol_dishe_2,
              symbol_dishe_name_2_uk,
              symbol_dishe_name_2_ru,
              symbol_dishe_3,
              symbol_dishe_name_3_uk,
              symbol_dishe_name_3_ru)
    string_list = list_1 + list_2
    return string_list


async def add_dishe():
    key_id = 1
    list_temp = []

    list_temp.append(value_string(
        num_category=1,
        name_id=key_id,
        name_uk='Гарбузовий крем-суп з чипсами з хамону',
        name_ru='Тыквенный крем-суп с чипсами из хамона',
        photo='https://sunray.ua/tmp/cache/images/c1/ce5/c1ce55a411e1a4fd1dbcd3486e3ad7d0.jpg',
        price='160',
        weight='220',
        specification_uk='Вершки, шпинат, насіння сонишника, чіпси з хамону.',
        specification_ru='Сливки, шпинат, семена подсолнуха, чипсы из хамона.',
        ingredients='{"ingredients": [{"name_uk": "Вершки", "name_ru": "Сливки",'
                    '"price": "10", "quantity": "1", "weight": "5"}, '
                    '{"name_uk": "Шпинат", "name_ru": "Шпинат", '
                    '"price": "15", "quantity": "1", "weight": "10"}, '
                    '{"name_uk": "Насіння сонишника", "name_ru": "Семена подсолнуха",'
                    '"price": "5", "quantity": "1", "weight": "5"}, '
                    '{"name_uk": "Чіпси з хамону", "name_ru": "Чипси из хамона",'
                    '"price": "5", "quantity": "1", "weight": "5"}]}',
        symbol_dishe='🆕',
        symbol_dishe_2='-',
        symbol_dishe_3='-'
    ))
    key_id += 1

    list_temp.append(value_string(
        num_category=1,
        name_id=key_id,
        name_uk='Червоний карі з куркою та грибами',
        name_ru='Красный карри с курицей и грибами',
        photo='https://sunray.ua/tmp/cache/images/2e/ac9/2eac9fda7dcdd0fea8280962c07b3b59.jpg',
        price='175',
        weight='300',
        specification_uk='Бульйон червоний карі, гречана локшина, кінза.',
        specification_ru='Бульон красный карри, гречневая лапша, кинза',
        ingredients='{"ingredients": [{"name_uk": "Бульйон червоний карі", "name_ru": "Бульон красный карри",'
                    '"price": "180", "quantity": "1", "weight": "180"}, '
                    '{"name_uk": "Гречана локшина", "name_ru": "Гречневая лапша", '
                    '"price": "100", "quantity": "1", "weight": "10"}, '
                    '{"name_uk": "Кінза", "name_ru": "Кинза",'
                    '"price": "10", "quantity": "1", "weight": "5"}]}',
        symbol_dishe='🆕',
        symbol_dishe_2='🌶'))
    key_id += 1

    list_temp.append(value_string(
        num_category=1,
        name_id=key_id,
        name_uk='Курячий бульйон з овочами',
        name_ru='Куриный бульон с овощами',
        photo='https://sunray.ua/tmp/cache/images/02/b63/02b631c73bcdb41d24e471965b269bb3.jpg',
        price='140',
        weight='300',
        specification_uk='Курятина, паста.',
        specification_ru='Курятина, паста.',
        ingredients='{"ingredients": [{"name_uk": "Курятина", "name_ru": "Курятина",'
                    '"price": "100", "quantity": "1", "weight": "150"}, '
                    '{"name_uk": "Паста", "name_ru": "Паста", '
                    '"price": "40", "quantity": "1", "weight": "150"}]}'))
    key_id += 1

    list_temp.append(value_string(
        num_category=2,
        name_id=key_id,
        name_uk='Яйця Бенедикт з лососем та Голландським соусом',
        name_ru='Яйца Бенедикт с лососем и Голландским соусом',
        photo='https://sunray.ua/tmp/cache/images/7e/5c3/7e5c3f8d908dccfd960fc0b5661ff778.jpg',
        price='245',
        weight='270',
        specification_uk='Круасан, шпинат міні, ікра лосося, олія петрушки, базилік.',
        specification_ru='Круассан, шпинат мини, икра лосося, масло петрушки, базилик.',
        ingredients='{"ingredients": [{"name_uk": "Круасан", "name_ru": "Круассан",'
                    '"price": "130", "quantity": "1", "weight": "100"}, '
                    '{"name_uk": "Шпинат міні", "name_ru": "Шпинат мини", '
                    '"price": "20", "quantity": "1", "weight": "20"}, '
                    '{"name_uk": "Ікра лосося", "name_ru": "Икра лосося",'
                    '"price": "100", "quantity": "1", "weight": "30"} , '
                    '{"name_uk": "Олія петрушки", "name_ru": "Масло петрушки",'
                    '"price": "5", "quantity": "1", "weight": "5"}, '
                    '{"name_uk": "Базилік", "name_ru": "Базилик",'
                    '"price": "5", "quantity": "1", "weight": "15"}]}'))
    key_id += 1

    list_temp.append(value_string(
        num_category=2,
        name_id=key_id,
        name_uk='Тост з сиром, шинкою та трюфельним маслом',
        name_ru='Тост с сыром, ветчиной и трюфельным маслом',
        photo='https://retsept-prigotovleniya.ru/uploads/posts/2019-01/1548140492_1.jpg',
        price='160',
        weight='180'))
    key_id += 1

    list_temp.append(value_string(
        num_category=2,
        name_id=key_id,
        name_uk='Млинці з бананом та шоколадом',
        name_ru='Блины с бананом и шоколадом',
        photo='http://v.img.com.ua/nxs76/b/600x500/3/e8/eea1868f245ee718b4a19d894a7f3e83.jpg',
        price='120',
        weight='230'))
    key_id += 1

    list_temp.append(value_string(
        num_category=3,
        name_id=key_id,
        name_uk='Салат з авокадо та креветками',
        name_ru='Салат из авокадо и креветками',
        photo='https://sunray.ua/tmp/cache/images/d2/e9f/d2e9f7154b18faea593499609e0b9409.jpg',
        price='230',
        weight='220',
        specification_uk='Томати, соус на основі японського майонезу, імбир, кінза.',
        specification_ru='Томаты, соус на основе японского майонеза, имбирь, кинза.',
        ingredients='{"ingredients": [{"name_uk": "Томати", "name_ru": "Томаты",'
                    '"price": "20", "quantity": "1", "weight": "30"}, '
                    '{"name_uk": "Соус на основі японського майонезу", '
                    '"name_ru": "Соус на основе японского майонеза", '
                    '"price": "10", "quantity": "1", "weight": "20"}, '
                    '{"name_uk": "Імбир", "name_ru": "Имбирь",'
                    '"price": "15", "quantity": "1", "weight": "30"} , '
                    '{"name_uk": "Кінза", "name_ru": "Кинза",'
                    '"price": "5", "quantity": "1", "weight": "5"}]}',
        symbol_dishe='🦐'))
    key_id += 1

    list_temp.append(value_string(
        num_category=3,
        name_id=key_id,
        name_uk='М’ясне асорті з гріссіні',
        name_ru='Мясное ассорти с гриссини',
        photo='https://image.freepik.com/free-photo/cold-cuts-and-cheese-are-served-on-a-tray-on-a-table-with-white'
              '-wine-crackers-grissini-and-taralli-with-aromatic-herbs-on-a-blue-linen-festive-tablecloth_230432-364'
              '.jpg',
        price='250',
        weight='150'))
    key_id += 1

    list_temp.append(value_string(
        num_category=3,
        name_id=key_id,
        name_uk='Асорті сирів з медом',
        name_ru='Ассорти сыров с медом',
        photo='https://image.freepik.com/free-photo/assorted-cheeses-with-honey-and-nuts_135427-2227.jpg',
        price='250',
        weight='220',
        symbol_dishe='🌰'))
    key_id += 1

    list_temp.append(value_string(
        num_category=4,
        name_id=key_id,
        name_uk='Брускета з лососем, авокадо та червоною ікрою',
        name_ru='Брускетты с лососем, авокадо и красной икрой',
        photo='https://primamedia.gcdn.co/f/main/1986/1985249.jpg',
        price='225',
        weight='230',
        specification_uk='Гречаний хліб, огірок, крем сир, кріп, оливкова олія.',
        specification_ru='Гречневый хлеб, огурец, крем сыр, укроп, оливковое масло.',
        ingredients='{"ingredients": [{"name_uk": "Гречаний хліб", "name_ru": "Гречневый хлеб",'
               '"price": "20", "quantity": "1", "weight": "10"}, '
               '{"name_uk": "Огірок", "name_ru": "Огурец", '
               '"price": "10", "quantity": "1", "weight": "20"}, '
               '{"name_uk": "Крем сир", "name_ru": "Крем сыр",'
               '"price": "30", "quantity": "1", "weight": "20"} , '
               '{"name_uk": "Кріп", "name_ru": "Укроп",'
               '"price": "5", "quantity": "1", "weight": "10"}, '
               '{"name_uk": "Оливкова олія", "name_ru": "Оливковое масло",'
               '"price": "0", "quantity": "1", "weight": "5"}]}'))
    key_id += 1

    list_temp.append(value_string(
        num_category=4,
        name_id=key_id,
        name_uk='Авокадо тост з томатами та базиліком',
        name_ru='Авокадо тост с томатами и базиликом',
        photo='https://image.freepik.com/free-photo/avocado-toasts-with-arugula-and-cherry-tomatoes_84130-5839.jpg',
        price='185',
        weight='190',
        specification_uk='Гречаний хліб, базилік, оливкова олія.',
        specification_ru='Гречневый хлеб, базилик, оливковое масло.',
        ingredients='{"ingredients": [{"name_uk": "Гречаний хліб", "name_ru": "Гречневый хлеб",'
               '"price": "20", "quantity": "1", "weight": "10"}, '
               '{"name_uk": "Базилік", "name_ru": "Базилик", '
               '"price": "0", "quantity": "1", "weight": "10"}, '
               '{"name_uk": "Оливкова олія", "name_ru": "Оливковое масло",'
               '"price": "0", "quantity": "1", "weight": "5"}]}'))
    key_id += 1

    list_temp.append(value_string(
        num_category=5,
        name_id=key_id,
        name_uk='Лосось з японським рисом та соусом Шисо',
        name_ru='Лосось с японским рисом и соусом Шисо',
        photo='http://glossy.ru/userfiles/pub_images/3535%20(8).jpg',
        price='295',
        weight='250',
        specification_uk='Листя лайму, кінза, базилік.',
        specification_ru='Листья лайма, кинза, базилик.',
        ingredients='{"ingredients": [{"name_uk": "Листя лайму", "name_ru": "Листья лайма",'
               '"price": "20", "quantity": "1", "weight": "10"}, '
               '{"name_uk": "Кінза", "name_ru": "Кинза", '
               '"price": "10", "quantity": "1", "weight": "20"}, '
               '{"name_uk": "Базилік", "name_ru": "Базилик",'
               '"price": "0", "quantity": "1", "weight": "20"}]}',
        symbol_dishe='🆕'))
    key_id += 1

    list_temp.append(value_string(
        num_category=5,
        name_id=key_id,
        name_uk='Котлета з телятини з листям салату',
        name_ru='Котлета из телятины с листьями салата',
        photo='https://proxy10.online.ua/retsepty/r3-827968506d/big56e34365b3d78.jpg',
        price='270',
        weight='200',
        specification_uk='Салат міні Романо, кінза, м’ята, гірчиця, базилік.',
        specification_ru='Салат мини Романо, кинза, мята, горчица, базилик.',
        ingredients='{"ingredients": [{"name_uk": "Салат міні Романо", "name_ru": "Салат мини Романо",'
               '"price": "80", "quantity": "1", "weight": "100"}, '
               '{"name_uk": "Кінза", "name_ru": "Кинза", '
               '"price": "10", "quantity": "1", "weight": "20"}, '
               '{"name_uk": "М’ята", "name_ru": "Мята", '
               '"price": "10", "quantity": "1", "weight": "20"}, '
               '{"name_uk": "Гірчиця", "name_ru": "Горчица", '
               '"price": "10", "quantity": "1", "weight": "10"}, '
               '{"name_uk": "Базилік", "name_ru": "Базилик",'
               '"price": "0", "quantity": "1", "weight": "20"}]}',
        symbol_dishe='🆕'))
    key_id += 1

    list_temp.append(value_string(
        num_category=6,
        name_id=key_id,
        name_uk='Класичні / авторські / морозиво / сорбети',
        name_ru='Классические / авторские / мороженое / сорбеты',
        photo='https://grandkulinar.ru/uploads/posts/2018-11/1541436368_luchshie-deserty-dlya-piknika-100-receptov.jpg',
        price='0',
        weight='0',
        specification_uk='В асортименті',
        specification_ru='В ассортименте'))
    key_id += 1

    list_temp.append(value_string(
        num_category=7,
        name_id=key_id,
        name_uk='Еспресо',
        name_ru='Эспрессо',
        photo='https://www.archi.kh.ua/assets/images/products/174/espresso.jpg',
        price='55',
        weight='30'))
    key_id += 1

    list_temp.append(value_string(
        num_category=7,
        name_id=key_id,
        name_uk='Допіо',
        name_ru='Доппио',
        photo='https://coffeetee.ru/wp-content/uploads/2019/05/kofe-doppio-dvoynoy-espresso.jpg',
        price='100',
        weight='60'))
    key_id += 1

    list_temp.append(value_string(
        num_category=7,
        name_id=key_id,
        name_uk='Капучино',
        name_ru='Капучино',
        photo='https://coffeemaniya.com/wp-content/uploads/2016/05/%D0%BA%D0%BE%D1%84%D0%B5-%D0%BA%D0%B0%D0%BF%D1%83'
              '%D1%87%D0%B8%D0%BD%D0%BE.jpg',
        price='80',
        weight='120'))
    key_id += 1

    list_temp.append(value_string(
        num_category=7,
        name_id=key_id,
        name_uk='Капучино на рослинному молоці',
        name_ru='Капучино на растительном молоке',
        photo='https://coffeemaniya.com/wp-content/uploads/2016/05/%D0%BA%D0%BE%D1%84%D0%B5-%D0%BA%D0%B0%D0%BF%D1%83'
              '%D1%87%D0%B8%D0%BD%D0%BE.jpg',
        price='90',
        weight='120'))
    key_id += 1

    list_temp.append(value_string(
        num_category=7,
        name_id=key_id,
        name_uk='Лате',
        name_ru='Латте',
        photo='https://shop.tastycoffee.ru/files/shares/data/blog/capuccino-latte-flatwhite/image4.jpg',
        price='85',
        weight='180'))
    key_id += 1

    list_temp.append(value_string(
        num_category=7,
        name_id=key_id,
        name_uk='Лате на рослинному молоці',
        name_ru='Латте на растительном молоке',
        photo='https://shop.tastycoffee.ru/files/shares/data/blog/capuccino-latte-flatwhite/image4.jpg',
        price='95',
        weight='180'))
    key_id += 1

    list_temp.append(value_string(
        num_category=7,
        name_id=key_id,
        name_uk='Флет вайт',
        name_ru='Флет уайт',
        photo='https://shop.tastycoffee.ru/files/shares/data/blog/capuccino-latte-flatwhite/image100.jpg',
        price='100',
        weight='120'))
    key_id += 1

    list_temp.append(value_string(
        num_category=7,
        name_id=key_id,
        name_uk='Флет вайт на рослинному молоці',
        name_ru='Флэт уайт на растительном молоке',
        photo='https://shop.tastycoffee.ru/files/shares/data/blog/capuccino-latte-flatwhite/image100.jpg',
        price='110',
        weight='120'))
    key_id += 1

    list_temp.append(value_string(
        num_category=8,
        name_id=key_id,
        name_uk='V60 пуровер',
        name_ru='V60 пуровер',
        photo='https://tastybar.ru/wa-data/public/blog/plugins/logopost/images/2EWQOOxKIB.JPG',
        price='90',
        weight='250'))
    key_id += 1

    list_temp.append(value_string(
        num_category=8,
        name_id=key_id,
        name_uk='V60 пуровер',
        name_ru='V60 пуровер',
        photo='https://tastybar.ru/wa-data/public/blog/plugins/logopost/images/2EWQOOxKIB.JPG',
        price='120',
        weight='400'))
    key_id += 1

    list_temp.append(value_string(
        num_category=8,
        name_id=key_id,
        name_uk='Аеропрес',
        name_ru='Аэропрес',
        photo='https://coffeesite.kz/wp-content/uploads/2020/03/aeropress-retailers-and-distributors-header-002'
              '-768x439.jpg',
        price='85',
        weight='250'))
    key_id += 1

    list_temp.append(value_string(
        num_category=8,
        name_id=key_id,
        name_uk='Сифон',
        name_ru='Сифон',
        photo='https://ic.pics.livejournal.com/adavixen/66399196/12929/12929_original.jpg',
        price='125',
        weight='400'))
    key_id += 1

    list_temp.append(value_string(
        num_category=8,
        name_id=key_id,
        name_uk='Джезва',
        name_ru='Джезва',
        photo='https://image.freepik.com/free-photo/fresh-breved-coffee-in-cezve-woman-s-hand-pours-coffee-into-white'
              '-cup_105596-1548.jpg',
        price='70',
        weight='55'))
    key_id += 1

    list_temp.append(value_string(
        num_category=8,
        name_id=key_id,
        name_uk='Фільтр кава',
        name_ru='Фильтр кофе',
        photo='https://kofella.net/images/stories/kofevarka/bumazhnyie-filtryi-dlya-kofevarki.jpg',
        price='85',
        weight='200'))
    key_id += 1

    list_temp.append(value_string(
        num_category=9,
        name_id=key_id,
        name_uk='Ванільний раф',
        name_ru='Ванильный раф',
        photo='http://coffeecard.info/wp-content/uploads/2015/03/raf-coffee-recipe-mini.jpg',
        price='90',
        weight='180'))
    key_id += 1

    list_temp.append(value_string(
        num_category=9,
        name_id=key_id,
        name_uk='Какао',
        name_ru='Какао',
        photo='https://www.gastronom.ru/binfiles/images/20181128/b2c3fa61.jpg',
        price='60',
        weight='200'))
    key_id += 1

    list_temp.append(value_string(
        num_category=9,
        name_id=key_id,
        name_uk='Какао на рослинному молоці',
        name_ru='Какао на растительном молоке',
        photo='https://www.gastronom.ru/binfiles/images/20181128/b2c3fa61.jpg',
        price='80',
        weight='200'))
    key_id += 1

    list_temp.append(value_string(
        num_category=9,
        name_id=key_id,
        name_uk='Капуоранж',
        name_ru='Капуоранж',
        photo='https://stoneforest.ru/wp-content/uploads/2017/03/%D0%BA%D0%BE%D1%84%D0%B5-%D1%81-%D1%81%D0%BE%D0%BA'
              '%D0%BE%D0%BC-1-696x378.jpg',
        price='75',
        weight='120'))
    key_id += 1

    list_temp.append(value_string(
        num_category=9,
        name_id=key_id,
        name_uk='Матча лате',
        name_ru='Матча латте',
        photo='https://m.gemini.ua/wp-content/uploads/2019/08/japanese-green-tea-latte-white-cup-against-white'
              '-background_23-2148066999.jpg',
        price='85',
        weight='180'))
    key_id += 1

    list_temp.append(value_string(
        num_category=9,
        name_id=key_id,
        name_uk='Матча лате на рослинному молоці',
        name_ru='Матча латте на растительном молоке',
        photo='https://m.gemini.ua/wp-content/uploads/2019/08/japanese-green-tea-latte-white-cup-against-white'
              '-background_23-2148066999.jpg',
        price='95',
        weight='180'))
    key_id += 1

    list_temp.append(value_string(
        num_category=9,
        name_id=key_id,
        name_uk='Колд Брю',
        name_ru='Колд Брю',
        photo='https://kofella.net/images/stories/vseokofe/kofe-kold-bryu.jpg',
        price='150',
        weight='200'))
    key_id += 1

    list_temp.append(value_string(
        num_category=9,
        name_id=key_id,
        name_uk='Лимонади в асортименті',
        name_ru='Лимонады в ассортименте',
        photo='https://zira.uz/wp-content/uploads/2019/05/citrusoviy-limonad-2.jpg',
        price='80',
        weight='220'))
    key_id += 1

    list_temp.append(value_string(
        num_category=9,
        name_id=key_id,
        name_uk='Фреш в асортименті',
        name_ru='Фреш в ассортименте',
        photo='https://shkolazhizni.ru/img/content/i174/174912_big.jpg',
        price='90',
        weight='250'))
    key_id += 1

    list_temp.append(value_string(
        num_category=9,
        name_id=key_id,
        name_uk='Вода VODA.UA',
        name_ru='Вода VODA.UA',
        photo='https://edagoroda.com/wp-content/uploads/2020/11/Voda-UA-2021-Bottle.jpg',
        price='45',
        weight='400',
        specification_uk='газована / не газована',
        specification_ru='газированная / негазированная'))
    key_id += 1

    list_temp.append(value_string(
        num_category=9,
        name_id=key_id,
        name_uk='Чай в асортименті',
        name_ru='Чай в ассортименте',
        photo='https://99px.ru/sstorage/53/2014/08/tmb_108049_4883.jpg',
        price='80',
        weight='400'))
    key_id += 1

    for i in list_temp:
        if await Dishes.select('name_id').where(Dishes.name_id == int(i[5])).gino.scalar() == int(i[5]):
            print("Походу есть")
        else:
            print("Добавляю")
            await add_dishes(category_id=int(i[0]),
                             category_code=i[1],
                             category_symbol=i[2],
                             category_name_uk=i[3],
                             category_name_ru=i[4],
                             name_id=int(i[5]),
                             name_uk=i[6],
                             name_ru=i[7],
                             photo=i[8],
                             price=int(i[9]),
                             weight=int(i[10]),
                             specification_uk=i[11],
                             specification_ru=i[12],
                             ingredients=i[13],
                             symbol_dishe=i[14],
                             symbol_dishe_name_uk=i[15],
                             symbol_dishe_name_ru=i[16],
                             symbol_dishe_2=i[17],
                             symbol_dishe_name_2_uk=i[18],
                             symbol_dishe_name_2_ru=i[19],
                             symbol_dishe_3=i[20],
                             symbol_dishe_name_3_uk=i[21],
                             symbol_dishe_name_3_ru=i[22]
                             )

from utils.db_api.models import Dishes


async def categories_text(key, lang):
    if lang == "ru":
        indevs = "В разработке. \nСкоро будет. \nХорошего Вам дня. \n :-)"
    else:
        indevs = "В розробці. \nСкоро буде. \nГарного Вам настрою. \n :-)"
    text = " "
    if key == 1:
        text = await menu_text()
    if key == 2:
        text = indevs
    if key == 3:
        text = indevs
    if key == 4:
        text = indevs
    if key == 5:
        text = indevs
    if key == 6:
        text = indevs
    if key == 7:
        text = indevs
    if key == 8:
        text = await choise_lang_text()
    return text


async def choise_lang_text():
    text = "Оберіть мову\nВыберите язык"
    return text


async def menu_text():
    text = "<b>📖 Меню:</b>"
    return text


async def card_dishe_text(lang,
                          dishe_id):
    lang_name = "name_" + lang
    lang_specification = "specification_" + lang
    price = await Dishes.select('price').where(Dishes.name_id == dishe_id).gino.scalar()
    photo = await Dishes.select('photo').where(Dishes.name_id == dishe_id).gino.scalar()
    name = await Dishes.select(lang_name).where(Dishes.name_id == dishe_id).gino.scalar()
    sym_1 = await Dishes.select("symbol_dishe").where(Dishes.name_id == dishe_id).gino.scalar()
    sym_2 = await Dishes.select("symbol_dishe_2").where(Dishes.name_id == dishe_id).gino.scalar()
    sym_3 = await Dishes.select("symbol_dishe_3").where(Dishes.name_id == dishe_id).gino.scalar()
    symvols = ""
    if sym_1 != "-":
        symvols = symvols + sym_1 + " "
    if sym_2 != "-":
        symvols = symvols + sym_2 + " "
    if sym_3 != "-":
        symvols = symvols + sym_3 + " "
    specification = await Dishes.select(lang_specification).where(Dishes.name_id == dishe_id).gino.scalar()
    if specification == "-":
        specification = " "
    else:
        specification = specification + "\n"
    quality = 0
    # purchase = json.loads(await Users.select('choice').where(Users.chat_id == chat_id).gino.scalar())
    # for key2 in purchase.keys():
    #     if int(key2) == int(dishe_id):
    #         quality = quality + purchase[key2]["quantity"]
    message_text = (f'<a href="{photo}"> </a>'
                    f'  \n'
                    f'{symvols}<b>{name}</b>\n'
                    f'<i>{specification} </i>'
                    f'<b>{price}₴ </b>\n'
                    f' 🛒 = {quality} шт.\n')

    return message_text

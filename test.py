# # import asyncio
# # import json
# #
# # from utils.db_api.models import Dishes
# #
# #
# # async def test_ing(name_uk="Гарбузовий крем-суп з чипсами з хамону"):
# #     ingreds = json.loads(await Dishes.select('ingredients').where(Dishes.name_uk == name_uk).gino.scalar())["ingredients"]
# #     # print(type(test))
# #     for key in ingreds:
# #         print(key)
# #         # print(type(i))
# #         print("Інгрідієнт: " + str(key["name_uk"]) + " коштує " + str(key["price"]) + " грн.")
# #         pass
#
#
# cchoice = '{' \
#          '"-":{' \
#          '"name_uk": "-", "name_ru": "-",' \
#          '"price": "10", "quantity": "1", "weight": "5"' \
#          '},' \
#          '}'
#
#
# choice = {
#     "-": {
#         "index": "-",
#         "name_uk": "-",
#         "name_ru": "-",
#         "price": 0,
#         "quantity": 0,
#         "weight": "5",
#         "ingredients": [
#             {"name_uk": "-", "name_ru": "-",
#              "price": "0", "quantity": "0", "weight": "0"}
#         ]
#     },
# }

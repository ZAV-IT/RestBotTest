# import asyncio
# import asyncpg
# import logging
#
# from data.config import host, db_user, db_pass
#
# logging.basicConfig(
#     format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s',
#     level=logging.INFO
# )
#
#
# async def create_db():
#     create_db_command = open("create_db.sql", "r").read()
#
#     logging.info("Connecting to bd")
#     conn: asyncpg.Connection = await asyncpg.connect(
#         user=db_user,
#         password=db_pass,
#         host=host
#     )
#     await conn.execute(create_db_command)
#     logging.info("Table has been created")
#     await conn.close()
#
#
# async def create_pool():
#     return await asyncpg.create_pool(
#         user=db_user,
#         password=db_pass,
#         host=host
#     )
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(create_db())

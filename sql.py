
import asyncio
import asyncpg
import logging

from data.config import PGUSER, PGPASSWORD, ip


async def create_db():
    create_db_command = open("create_db.sql", "r").read()

    conn: asyncpg.Connection = await asyncpg.connect(user=PGUSER,
                                                     password=PGPASSWORD,
                                                     host=ip)
    try:
        await conn.execute(create_db_command)
    except asyncpg.exceptions.DuplicateTableError:
        pass
    await conn.close()
    logging.info("Table users created")


async def create_pool():
    return await asyncpg.create_pool(user=PGUSER,
                                     password=PGPASSWORD,
                                     host=ip)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_db())

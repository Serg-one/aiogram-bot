import asyncio
import asyncpg
import logging

from pathlib import Path
from data.config import IP, PG_USER, PG_PASS

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO,
                    )

sql_script = Path('utils/db_api/create_db.sql')


async def create_db():
    logging.info("Connecting to database...")

    create_db_command = open(sql_script, 'r').read()
    conn: asyncpg.Connection = await asyncpg.connect(
        user=PG_USER,
        password=PG_PASS,
        host=IP
    )
    await conn.execute(create_db_command)

    logging.info("Table was created.")
    await conn.close()


async def create_pool():
    return await asyncpg.create_pool(
        user=PG_USER,
        password=PG_PASS,
        host=IP
    )


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_db())

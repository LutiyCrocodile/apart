import asyncpg
from core.config import settings


async def read_all(table):
    try:
        connection = await asyncpg.connect(dsn=settings.DATABASE_URL)
        query = f'SELECT {table} FROM {settings.DB_SCHEMA}."{table}"'
        result = await connection.fetch(query)
        await connection.close()
        return result
    except Exception as e:
        print(f"[INFO]Error '{e}'")


async def insert_item(table, value):

    connection = await asyncpg.connect(dsn=settings.DATABASE_URL)
    stmt = f"INSERT INTO {settings.DB_SCHEMA}.{table}({table}) VALUES ({value})"
    result = await connection.execute(stmt)
    await connection.close()
    return result

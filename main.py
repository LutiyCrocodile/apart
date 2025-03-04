from sqlalchemy import select
from parser.parser import get_pars
from core.db_helper import db_engine

data = get_pars()
del data["url"]
del data["residential_complex"]
keys = data.keys()
items = data.items()


async def main():
    async with db_engine.engine.begin() as conn:
        result = conn.execute()


print(main())

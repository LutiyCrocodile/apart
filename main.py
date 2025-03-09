import asyncio

from sqlalchemy.util import await_only
from parser.parser import get_pars
from db_crud import crud


async def main():
    data = get_pars()
    del data["url"]
    del data["floor"]
    del data["floors_count"]
    del data["rooms_count"]
    del data["total_meters"]
    del data["price"]
    del data["residential_complex"]
    data["metro"] = data["underground"]
    del data["underground"]
    for table, value in data.items():
        result = await crud.read_all(table)
        if result:
            if table not in result:
                await crud.insert_item(table, value)
        else:
            await crud.insert_item(table, value)


if __name__ == "__main__":
    asyncio.run(main())

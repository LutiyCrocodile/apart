import asyncio

from sqlalchemy import text
from parser.parser import get_pars
from core.config import connection


async def pars_filtred():
    # какие данные берем из бд
    selected_values = {
        "deal_type": "deal_type",
        "underground": "underground",
    }
    rooms = (1, 2, 3, 4, 5, "studio")

    # конект с бд
    for key, value in selected_values.items():
        if key == "deal_type":
            async with connection() as session:
                fetch_query = text(
                    f"SELECT {value} FROM real_estate.{key}",
                )
                result = await session.execute(fetch_query)
                deal_type_list = result.scalars().all()
        elif key == "underground":
            async with connection() as session:
                fetch_query = text(
                    f"SELECT {value} FROM real_estate.{key}",
                )
                result = await session.execute(fetch_query)
                underground_list = result.scalars().all()

    # особые настройки для парсера
    additional_settings = {
        "start_page": 1,
        "end_page": 2,
        "metro": "Московский",
    }

    returning_flats = []

    # проходимся по данным из бд
    for room in rooms:
        for deal_type in deal_type_list:
            if deal_type == "rent":
                for underground in underground_list:
                    additional_settings["metro_station"] = underground
                    returning_flats.append(
                        get_pars(
                            rooms=room,
                            deal_type="rent_long",
                            additional_settings=additional_settings,
                        )
                    )
            else:
                for underground in underground_list:
                    additional_settings["metro_station"] = underground
                    returning_flats.append(
                        get_pars(
                            rooms=room,
                            deal_type="rent_long",
                            additional_settings=additional_settings,
                        )
                    )
    # вывод результата
    print(returning_flats, sep="\n")


asyncio.run(pars_filtred())

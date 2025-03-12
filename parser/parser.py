import cianparser


def get_pars(deal_type: str, rooms: int, additional_settings: dict) -> list[dict]:
    moscow_parser = cianparser.CianParser(location="Москва")
    data = moscow_parser.get_flats(
        deal_type=deal_type,
        rooms=rooms,
        with_saving_csv=False,
        additional_settings=additional_settings,
    )
    return data

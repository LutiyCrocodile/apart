import cianparser


def get_pars():
    moscow_parser = cianparser.CianParser(location="Москва")
    data = moscow_parser.get_flats(
        deal_type="sale",
        rooms=(1, 2),
        with_saving_csv=True,
        additional_settings={"start_page": 1, "end_page": 2},
    )
    return data[0]

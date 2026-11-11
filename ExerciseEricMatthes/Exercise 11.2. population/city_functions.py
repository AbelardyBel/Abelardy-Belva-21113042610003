def get_city_country(city, country, population=None):
    """Mengembalikan 'Kota, Negara', atau dengan populasi kalau diisi."""
    if population:
        return f"{city.title()}, {country.title()} \u2013 population {population}"
    else:
        return f"{city.title()}, {country.title()}"

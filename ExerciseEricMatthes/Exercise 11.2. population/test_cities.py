from city_functions import get_city_country

def test_city_country():
    """Apakah 'santiago' dan 'chile' menghasilkan 'Santiago, Chile'?"""
    hasil = get_city_country('santiago', 'chile')
    assert hasil == 'Santiago, Chile'

def test_city_country_population():
    """Apakah populasi ikut tampil kalau diisi?"""
    hasil = get_city_country('santiago', 'chile', population=5000000)
    assert hasil == 'Santiago, Chile \u2013 population 5000000'

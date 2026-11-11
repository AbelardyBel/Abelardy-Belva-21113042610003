from city_functions import get_city_country

def test_city_country():
    """Apakah 'santiago' dan 'chile' menghasilkan 'Santiago, Chile'?"""
    hasil = get_city_country('santiago', 'chile')
    assert hasil == 'Santiago, Chile'

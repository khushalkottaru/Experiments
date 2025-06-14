'''Tests the city_functions module.'''
from city_functions import get_formatted_location


def test_city_country():
    '''Do places like 'Santiago, Chile' work?'''
    location = get_formatted_location('santiago', 'chile')
    assert location == 'Santiago, Chile'

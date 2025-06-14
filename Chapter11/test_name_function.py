from name_function import get_formatted_name


def test_first_last_name():
    '''Do names like 'Janis Joplin' work?'''
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'


def test_first_middle_last():
    '''Do names like 'Wolfgang Amadeus Mozart' work?'''
    formatted_name = get_formatted_name(
        'wolfgang', middle='amadeus', last='mozart')
    assert formatted_name == 'Wolfgang Amadeus Mozart'

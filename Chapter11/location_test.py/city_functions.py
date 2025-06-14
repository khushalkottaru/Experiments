def get_formatted_location(city, country, population=''):
    '''Prints a formatted location.'''
    if population:
        formatted_location = f'{city}, {country} - population {population}'
        return formatted_location.title()
    else:
        formatted_location = f'{city}, {country}'
        return formatted_location.title()

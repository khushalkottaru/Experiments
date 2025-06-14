from name_function import get_formatted_name

print('Enter "q" at any time to quit.')
while True:
    first = input('\nPlease give me a first name: ')
    last = input('\nPlease give me a last name: ')
    if first or last == 'q':
        break
    formatted_name = get_formatted_name(first=first, last=last)
    print(f'\tNeatly formatted name: {formatted_name}')

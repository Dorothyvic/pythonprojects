def phone():
    numbers = {
            '1': 'one',
            '2': 'two',
            '3': 'three',
            '4': 'four'
            }
    phone = input('Phone: ')
    for number in phone:
        return numbers.get(number, '!'), end=' '
    print(phone())

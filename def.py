def phone_converter():
    numbers = {
            '1': 'one',
            '2': 'two',
            '3': 'three',
            '4': 'four'
            }
    for number in num:
        print(numbers.get(number, '!'), end=' ')


num = input('Phone: ')
phone_converter()



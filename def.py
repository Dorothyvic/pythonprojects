def phone_converter(phone):
    numbers = {
            '1': 'one',
            '2': 'two',
            '3': 'three',
            '4': 'four'
            }
    for number in phone:
        return numbers.get(number, '!') + ' '


phone = input('Phone: ')
print(phone_converter(phone))



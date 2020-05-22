# A simple python program that converts phone numbers to their word equivalent

# Dictionary containing numbers and their word equivalents against which we compare
numbers = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four'
}

# Request user input
phone = input('Please enter your phone number: ')

# Compare and return word equivalent of each number
print("Your number is")
for number in phone:
    print(numbers.get(number, '!'), end=' ')

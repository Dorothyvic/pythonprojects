# a simple program to ask the user's name, favourite colour and age
class App:
    def person(self):
        name = input('What is your name? ')
        colour = input('What is your favourite colour? ')
        return name + ' likes ' + colour

    def birthyear(self):
        birth_year = int(input('Birth year: '))
        age = 2019 - birth_year
        return f'You are {age} years old\n'

# A simple program to calculate the house down payment when the user has good credit
    def house_pay(self):
        price = 1000000
        has_good_credit = True
        if has_good_credit:
            down_payment = 0.1 * price
        else:
            down_payment = 0.2 * price
        return f' Your down payment is ${down_payment}\n'

# A simple program to determine the user's name length
    def patient(self):
        name = input('What is your name: ')
        if len(name) < 3:
            return 'Name must be at least three characters\n'
        elif len(name) > 50:
            return 'Name can be a maximum of 50 characters\n'
        else:
            return 'Name looks good!\n'

# A simple program to convert the user's weight to kilograms and pounds
    def weightconverter(self):
        weight = int(input('What is your weight: '))
        unit = input('In (L)bs or (K)kg: ')
        if unit.upper() == 'L':
            cal = 0.45 * weight
            return f'You are {cal}kg\n'
        else:
            cal = 100 * weight
            return f'You are {cal}bs\n'

# A simple guessing game program
    def guess(self):
        secret_number = 9
        guess_count = 0
        guess_limit = 3
        while guess_count < guess_limit:
            guess = int(input('Guess: '))
            guess_count += 1
            if guess == secret_number:
                print('You won\n')
                break
        else:
            print('Sorry, you failed\n')

    # A simple python program that converts phone numbers to their word equivalent

    # Dictionary containing numbers and their word equivalents against which we compare
    def phone_converter(self):
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
            print(numbers.get(number, '!') + ' ')

# A simple car game program
    def cargame(self):
        started = False
        while True:
            command = input('> ').lower()
            if command == 'help':
                print('''
start - to start the car
stop - to stop the car
quit - to exit''')
            elif command == 'start':
                if started:
                    print('Car has already started\n')
                else:
                    started = True
                    print('Car started.... ready to go!\n')
            elif command == 'stop':
                if not started:
                    print('Car has already stopped\n')
                else:
                    started = False
                    print('Car stopped\n')
            elif command == 'quit':
                break
            else:
                print("Sorry, I don't understand that\n")


app = App()
print("USER'S NAME, FAVOURITE COLOUR AND AGE")
print(app.person())
print(app.birthyear())
print('****HOUSE DOWN PAYMENT PROGRAM****')
print(app.house_pay())
print("****PATIENTS' NAME PROGRAM****")
print(app.patient())
print('****WEIGHT CONVERTER PROGRAM****')
print(app.weightconverter())
print('****GUESSING GAME PROGRAM****')
print('Please guess the right number because you are given three chances of guessing')
app.guess()
print('****PHONE NUMBER CONVERTER PROGRAM****')
app.phone_converter()
print('****CAR GAME PROGRAM****')
print('FOR HELP, YOU CAN TYPE "help"')
app.cargame()


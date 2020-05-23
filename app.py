class App:
    def person(self):
        name = input('What is your name? ')
        colour = input('What is your favourite colour? ')
        return name + ' likes ' + colour

    def birthyear(self):
        birth_year = int(input('Birth year: '))
        age = 2019 - birth_year
        return age

    def house_pay(self):
        price = 1000000
        has_good_credit = True
        if has_good_credit:
            down_payment = 0.1 * price
        else:
            down_payment = 0.2 * price
        return f'Down payment: ${down_payment}'

    def patient(self):
        name = 'dorothy'
        if len(name) < 3:
            return 'Name must be at least three characters'
        elif len(name) > 50:
            return 'Name can be a maximum of 50 characters'
        else:
            return 'Name looks good!'

    def weightconverter(self):
        weight = int(input('Weight: '))
        unit = input('(L)bs or (K)kg: ')
        if unit.upper() == 'L':
            cal = 0.45 * weight
            return f'You are {cal}kg'
        else:
            cal = 100 * weight
            return f'You are {cal}bs'

    def

app = App()
print(app.person())
print(app.birthyear())
print(app.house_pay())
print(app.patient())
print(app.weightconverter())
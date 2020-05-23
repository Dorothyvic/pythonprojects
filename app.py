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
            print('Name must be at least three characters')
        elif len(name) > 50:
            print('Name can be a maximum of 50 characters')
        else:
            print('Name looks good!')


app = App()
print(app.person())
print(app.birthyear())
print(app.house_pay())
print(app.patient())
weight = int(input('Weight: '))
unit = input('(L)bs or (K)kg: ')
if unit.upper() == 'L':
    cal = 0.45 * weight
    print(f'You are {cal}kg')
else:
    cal = 100 * weight
    print(f'You are {cal}bs')

num = int(input('Enter number of elements to be inserted: '))
a = []
for x in range(0,num):
    number = int(input('Enter element: '))
    a.append(number)
    total = sum(a) / num
print(f'The average of the elements in the list is {total}')    

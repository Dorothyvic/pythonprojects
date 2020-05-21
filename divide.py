lower = int(input('Enter lower range limit: '))
upper = int(input('Enter upper range limit: '))
div = int(input('Enter number to be divided by: '))
for x in range(lower, upper):
    if x%div == 0:
        print(x)



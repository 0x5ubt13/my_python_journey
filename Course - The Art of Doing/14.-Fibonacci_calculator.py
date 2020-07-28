#!/usr/bin/env python3
x = 0
y = 0
z = 0
golden = [0, 1]

print('Welcome to the Fibonacci Calculator App!')
number = int(input('\nHow many digits of the Fibonacci Sequence would you like to compute?: '))

print('The first ' + str(number) + ' numbers of the Fibonacci Sequence are:')
for n in range(number):
    x = y + z
    if n == 1:
        x = 1
    if x and y != 0:
        golden.append(x/y)
    z = y
    y = x
    print(x)
    

# Alternative way to do fibonacci sequence with list in less lines:
# fib = [1, 1]
# for i in range(number-2):
#     new_fib = fib[i] + fib[i+1]
#     fib.append(new_fib)

print('\nThe corresponding Golden Ratio values are: ')

for ratio in golden:
    print(ratio)



    





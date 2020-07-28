#!/usr/bin/env python3
import math

fact_list = []
result = 1

print('Welcome to the Factorial Calculator App.')
factorial = int(input('What number would you like to compute the factorial of?: '))

for n in range(factorial+1):
    if n != 0:
        fact_list.append(str(n))
        result *= n 

print(fact_list)
fact_tuple = fact_list
print(fact_tuple)

miformula = '*'.join(fact_tuple)
print(miformula)

print('Here is the result from the math library:\nThe factorial of', factorial, 'is ' + str(math.factorial(factorial)) + '!\n')

print('Here is the result from my own algorithm:\nThe factorial of', factorial, 'is ' + str(result) + '!\n')

if math.factorial(factorial) == result:
    print('It is shown twice that ' + str(factorial) + '! =', str(result), '(with excitement)')
else: print('Not matching')

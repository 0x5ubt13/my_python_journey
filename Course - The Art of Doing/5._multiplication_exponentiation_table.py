#!/usr/share/env python3

print('Welcome to 5ubt13\'s multiplication and exponentiation table program! \n')
name = input('Please enter your name: ').title().strip()
u_n = (float(input('\nPlease enter your desired number to operate: ')))


for n in range(1, 10):
    if n == 1:
        print(f'Multiplication table for {u_n}: \n')
    else: print(f'{u_n} * {n} = {u_n * n}')

for n in range(1, 10):
    if n == 1:
        print(f'\nExponent table for {u_n}: \n')
    else: print(f'{u_n} ** {n} = {u_n ** n}')

print(f'{name}, Math is cool!')
print((f'\t{name}, math is cool!').lower())
print((f'\t\t{name}, math is cool!').title())
print((f'\t\t\t{name}, math is cool!').upper())
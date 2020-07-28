#!usr/bin/env python3
import cmath

print('Welcome to the Quadratic Solver App.\n\nA quadratic equation is of the form ax^2 + bx + c = 0\nYour solutions can be real or complex numbers.\nA complex number has two parts: a + bj,\nWhere a is the real portion and bj is the imaginary portion.')
how_many = int(input('How many equations would you like to solve today?'))

for n in range(how_many):
    print('Solving equation #'+ str(n+1), '\n', '-'*20)
    a = float(input('Please enter your value of a (coefficient of x^2): '))
    b = float(input('Please enter your value of b (coefficient of x): '))
    c = float(input('Please enter your value of c (coefficient): '))
    print('\nThe solutions to', str(a) + 'x^2 +', str(b) + 'x +', str(c), 'are:\n')
    x1 = (-b + cmath.sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - cmath.sqrt(b**2 - 4*a*c)) / (2*a)
    
    print('\nThe solutions to ' + str(a) + 'x^2 +', str(b) + 'x + ' + str(c), '= 0 are:', '\n\t\tx1 = ' + str(x1), '\n\t\tx2= ' + str(x2), '')

    # 3 -5 -8 = 2.6, -1
    # 
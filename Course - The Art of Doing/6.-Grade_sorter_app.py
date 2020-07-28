#!/usr/bin/env python3

grades = []

print('Welcome to the Grade Sorter App!')

for i in range(4):
    grades.append(int(input(f'What is your grade number {i+1}: ')))

print('Your grades are:', grades)

print('Your grades from highest to lowest are:', sorted(grades, reverse=True))

print('The lowest two grades will now be dropped')
for i in range(2):
    print('Removed grade:', grades[-1])
    grades.pop()

print('Your remaining grades are: ' + str(grades[0]) + ',', grades[1])
print('Nice work! Your highest grade is a', grades[0]) 


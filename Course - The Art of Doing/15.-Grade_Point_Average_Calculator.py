#!/usr/bin/env python3
# Initializing our variables
grades = []
x = 0 
y = 0

# Get initial user input
print('Welcome to the Grade Point Average Calculator app!\n')
name = input('What is your name? ').title().strip()
n_grades = int(input('Now, how many grades would you like to enter? '))

#Loop to get user's grades
for n in range(n_grades):
    grades.append(int(input('Enter grade: ')))

# Sort grades, print them to the screen and return average variable
print('\nGrades Highest to lowest:')
grades.sort(reverse=True)
for grade in grades:
    print('\t', grade)
    x = x + grade
avg = x / len(grades)    

# Print a grade summary
print(f'\n{name}\'s Grade Summary:\n\tTotal number of Grades: ' + str(len(grades)) + '\n\tHighest Grade: ' + str(grades[0]) + '\n\tLowest Grade: ' + str(grades[len(grades)-1]) + '\n\tAverage: ' + str(avg))

# Getting a new average and calculate next needed grade to accomplish it
new_average = int(input('\nEnter your desired Average: '))
des_new = (new_average * (len(grades) + 1)) - x
print(f'\nGood luck, {name}!\nYou will need to get a {str(des_new)}')

# Make a copy of the original grades and swap out one of them
print('Let\'s see what your average could have been if you did better/worse on an assignment.')
change_from = int(input('What grade would you like to change? '))
change_to = int(input(f'What grade would you like to change {change_from} to: '))
new_grades = grades[:]
new_grades.remove(change_from)
new_grades.append(change_to)
new_grades.sort(reverse=True)

# New grades summary
print('\nNew grades from Highest to lowest:')
for grade in new_grades:
    print('\t', grade)
    y = y + grade
new_avg = y / len(new_grades)

print(f'\n{name}\'s New Grade Summary:\n\tTotal number of Grades: ' + str(len(new_grades)) + '\n\tHighest Grade: ' + str(grades[0]) + '\n\tLowest Grade: ' + str(grades[len(grades)-1]) + '\n\tAverage: ' + str(new_avg) + f'\nYour new average would be a {new_avg} compared to your real average of {avg}!\nThat is a change of ' + str(round((new_avg - avg), 2)) + ' points!\n\nToo bad your original grades are still the same!\n' + str(grades) + '\nYou should go ask for extra credit!')

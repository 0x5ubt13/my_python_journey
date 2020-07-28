#!/usr/bin/env python3

teachers = []
print('Welcome to your favourite teachers\' app!')
teachers.append(input('Please input your first favorite teacher: ').title())
teachers.append(input('Please input your second favorite teacher: ').title())
teachers.append(input('Please input your third favorite teacher: ').title())
teachers.append(input('Please input your fourth favorite teacher: ').title())

print('\nHere\'s your favorite teachers\' list: ', teachers)
print('Here\'s your favorite teachers\' list alphabetically: ', sorted(teachers))
print('Here\'s your favorite teachers\' list alphabetically reversed: \n', sorted(teachers, reverse=True))
print('\nYour top two teachers are:', teachers[0],'and', teachers[1])
print('Your next two favorite teachers are:', teachers[2],'and', teachers[3])
print('You have a total of', len(teachers), 'favorite teachers.\n')

no_longer = teachers[0]
teachers.insert(0, input(f'Oops, {no_longer} is no longer your first favorite teacher. Who is your new FAVORITE teacher: ').title())

print('\nHere\'s your favorite teachers\' list: ', teachers)
print('Here\'s your favorite teachers\' list alphabetically: ', sorted(teachers))
print('Here\'s your favorite teachers\' list alphabetically reversed: \n', sorted(teachers, reverse=True))
print('\nYour top two teachers are:', teachers[0],'and', teachers[1])
print('Your next two favorite teachers are:', teachers[2],'and', teachers[3])
print('You have a total of', len(teachers), 'favorite teachers.\n')

teachers.remove(input('You have decided you no longer like a teacher. Which teacher would you like to take off of the list: ').title())

print('\nHere\'s your favorite teachers\' list: ', teachers)
print('Here\'s your favorite teachers\' list alphabetically: ', sorted(teachers))
print('Here\'s your favorite teachers\' list alphabetically reversed: \n', sorted(teachers, reverse=True))
print('\nYour top two teachers are:', teachers[0],'and', teachers[1])
print('Your next two favorite teachers are:', teachers[2],'and', teachers[3])
print('You have a total of', len(teachers), 'favorite teachers.\n')
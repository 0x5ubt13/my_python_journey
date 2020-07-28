#!/usr/bin/env/ python3

pg = input('Who is your point guard?: ').title()
sg = input('Who is your small guard?: ').title()
sf = input('Who is your small forward?: ').title()
pf = input('Who is your point forward?: ').title()
center = input('Who is your center?: ').title()

print('\t\tYour starting 5 for the upcoming basketball season:')
print('\t\t\tPoint Guard:\t\t', pg)
print('\t\t\tSmall Guard:\t\t', sg)
print('\t\t\tSmall Forward:\t\t', sf)
print('\t\t\tPoint Forward:\t\t', pf)
print('\t\t\tCenter:\t\t\t\, center)

print('Oh no,', sg, 'is injured. \nYour roster only has 4 players.')
sg = input(f'Who will take {sg}\'s spot?: ').title()

print('\t\tYour starting 5 for the upcoming basketball season:')
print('\t\t\t\tPoint Guard:\t\t\t', pg)
print('\t\t\t\tSmall Guard:\t\t\t', sg)
print('\t\t\t\tSmall Forward:\t\t\t', sf)
print('\t\t\t\tPoint Forward:\t\t\t', pf)
print('\t\t\t\tCenter:\t\t\t\t', center)

print('Good luck', sg, 'you will do great!')
print('Your roster has now 5 players')

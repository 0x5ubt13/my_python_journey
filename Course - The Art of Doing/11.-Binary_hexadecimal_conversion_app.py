#!/usr/bin/env python3

decimal = []
hexadecimal = []
binary = []

print('Welcome to the Binary/Hexadecimal converter app!')
limit = int(input('Compute binary and hexadecimal values up to the following decimal number: '))
for i in range(limit):
    decimal.append(i)
    hexadecimal.append(hex(i))
    binary.append(bin(i))
print('Generating lists... Complete!')

slice_value_start = int(input('\nUsing slices, we will now show a portion of each list.\nWhat decimal number would you like to start at?: '))
slice_value_stop = int(input('What decimal number would you like to stop at?: ')) + 1

print(f'\nDecimal values from {slice_value_start} to {slice_value_stop - 1}:')
for i in range(slice_value_start, slice_value_stop):
    print(decimal[i])

print(f'\nBinary values from {slice_value_start} to {slice_value_stop - 1}:')
for i in range(slice_value_start, slice_value_stop):
    print(binary[i])

print(f'\nHexadecimal values from {slice_value_start} to {slice_value_stop - 1}:')
for i in range(slice_value_start, slice_value_stop):
    print(hexadecimal[i])

input(f'\nPlease press Enter to see all values from 1 to {limit}')
print('Decimal ---------- Binary ---------- Hexadecimal')
for i in range(limit + 1):
    print(f'{decimal[i+1]} ---------- {binary[i+1]} ---------- {hexadecimal[i+1]}')
        

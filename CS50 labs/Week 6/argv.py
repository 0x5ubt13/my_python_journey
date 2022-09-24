# How to take args in python
from sys import argv

counter = 0

print("Your args:")
for arg in argv:
    print(f"\t{counter}: {arg}")
    counter += 1

# If only 1 arg passed along the name of the program, print the first one
if len(argv) == 2:
    print(f"hello, {argv[1]}")
else:
    print(f"hello, world")
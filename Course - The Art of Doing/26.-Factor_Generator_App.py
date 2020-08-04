#/usr/bin/python3

print("Welcome to the Factor Generator App")
while True:
    i = 1
    factors = []
    key_number = int(input("\nEnter a number to determine all factors of it: "))
    print("Factors of " + str(key_number) + " are:")
    while i <= key_number:
        if key_number % i == 0:
            print(i)
            factors.append(i)
        i += 1
    print("\nIn summary:")
    for i in range((len(factors)+1)//2):
        print(factors[i], "*", factors[-i-1], '=', str(key_number))
    choice = input("Run again? (y/n) ")
    if choice == 'n':
        break
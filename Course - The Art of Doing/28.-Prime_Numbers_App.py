#/usr/bin python3

print('Welcome to the Prime Number App.')

while True:
    set_mode = input('''
    ************************
    *     Choose mode:     *
    *                      *
    *                      *
    * (1) Specific number  *
    *                      *
    *                      *
    * (2) Range of numbers *
    *                      *
    *                      *
    ************************
    Your choice: 
    ''')

    if set_mode == '1':
        number = int(input("Please enter a number to determine whether it's a Prime number: "))
        for i in range(2, number+1):
            if number % i == 0 and number != i:
                print(i)
                print(number, 'is not prime')
                break
            elif i == number:
                print(number, "is Prime!")

    elif set_mode == '2':
        primes = []
        numbers = input("Please enter two numbers to determine how many Prime numbers there are in their range: ").replace(",", "").strip().split()
        for i in range(int(numbers[0]), int(numbers[1])+1):
            for num in range(2, (i+1)):
                if i % num == 0 and num != i:
                    break
                elif num == i:
                    primes.append(num)
        choice = input("Do you want to see all the numbers that are Prime within the given range? (y/n): ").lower().strip()
        if choice == 'y': 
            for prime in primes:
                print(prime)            
    else:
        print("Wrong input.")
        continue

    again = input("Would you like to run the program again? (y/n): ").lower().strip()
    if again == 'n':
        break

print("Thanks for using the Prime Numbers App!")

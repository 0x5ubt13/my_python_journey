#/usr/bin python3

odd = []
even = []

print('Welcome to the Even Odd Numer Sorter App.')

while True:
    choice = list(input("Please enter your numbers: ").replace(",", " ").strip().split())
    print("---- Result Summary ----")
    for i in choice:
        if int(i) % 2 == 0:
            print(str(i), "is even!")
            even.append(i)
        else:
            print(i, "is odd!")
            odd.append(i)

    print("The following " + str(len(even)) + " numbers are even: ")
    for i in even:
        print(i)

    print("The following " + str(len(odd)) + " numbers are odd: ")
    for i in odd:
        print(i)
    breaking = input("Would you like to run the program again? (y/n) ")
    if breaking == 'n':
        break
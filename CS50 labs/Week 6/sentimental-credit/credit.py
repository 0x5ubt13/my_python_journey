import re


def get_cc():
    """Get credit card and return cc and potential type"""
    # Visa
    pattern1 = r'^\d{13}$'
    pattern2 = r'^[4]\d{15}$'

    # Amex
    pattern3 = r'^[3][47]\d{13}$'

    # Mastercard
    pattern4 = r'^[5][1-5]\d{14}$'

    # Loop
    while True:
        cc = input("Enter your credit card: ").strip()
        if re.search(pattern1, cc) or re.search(pattern2, cc):
            return cc, "VISA"
        if re.search(pattern3, cc) :
            return cc, "AMEX"
        if re.search(pattern4, cc):
            return cc, "MASTERCARD"
        if cc.isnumeric() == False:
            continue
        return cc, "INVALID"


def luhns_algo(cc):
    """Implementing Luhn's Algorithm"""
    # 1. Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products’ digits together.
    digits = [int(d) for d in cc]
    result = 0

    evens = digits[-2::-2]
    for num in evens:
        num *= 2
        for d in str(num):
            result += int(d)

    # 2. Add the sum to the sum of the digits that weren’t multiplied by 2.
    result += sum(digits[-1::-2])

    # 3. If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid!
    return result % 10


# Interesting ultra-simplified version of luhn's in python:
# def luhn(n):
#     r = [int(ch) for ch in str(n)][::-1]
#     return (sum(r[0::2]) + sum(sum(divmod(d*2,10)) for d in r[1::2])) % 10 == 0


def main():
    card, type = get_cc()
    print(type)
    if luhns_algo(card) == 0:
        print(luhns_algo(card))
        print(type)
    else:
        print("INVALID")


if __name__ == '__main__':
    main()

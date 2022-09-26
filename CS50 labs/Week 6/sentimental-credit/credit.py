import re

def get_cc():
    """Get credit card and return cc and potential type"""
    pattern1 = r'^\d{13}$' # visa
    pattern2 = r'^\d{15}$' # amex
    pattern3 = r'^\d{16}$' # visa or mastercard
    while True:
        cc = input("Enter your credit card: ").strip()
        if re.search(pattern1, cc):
            return cc, "VISA"
        if re.search(pattern2, cc):
            return cc, "AMEX"
        if re.search(pattern3, cc):
            if cc[0] == "4":
                return cc, "VISA"
            else:
                return cc, "MASTERCARD"
        return cc, "INVALID"


def luhns_algo(cc):
    """Implementing Luhn's Algorithm"""
    # 1. Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products’ digits together.
    digits = [int(d) for d in cc]
    pairs = []
    pair, odd, result, counter = 0, 0, 0, 0

    evens = digits[-2::-2]
    for num in evens:
        num *= 2
        for d in str(num):
            result += int(d)

    odds = digits[-1::-2]
    result += sum(odds)

    # 2. Add the sum to the sum of the digits that weren’t multiplied by 2.
    for num in pairs:
        for digit in str(num):
            pair += int(digit)
    result = pair + odd

    # 3. If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid!
    return result % 10

"""
:) identifies 4012888888881881 as VISA
:) identifies 4222222222222 as VISA
:) identifies 1234567890 as INVALID
:( identifies 369421438430814 as INVALID
    expected "INVALID\n", not "AMEX\n"
:) identifies 4062901840 as INVALID
:( identifies 5673598276138003 as INVALID
    expected "INVALID\n", not "MASTERCARD\n"
:( identifies 4111111111111113 as INVALID
    expected "INVALID\n", not "VISA\n"
:( identifies 4222222222223 as INVALID
    expected "INVALID\n", not "VISA\n"
"""


def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10


def main():
    card, type = get_cc()
    if luhns_algo(card) == 0:
        print(type)
    else:
        print("INVALID")


if __name__ == '__main__':
    main()
#!/usr/bin/python3

from sys import argv


def check():
    # Arg check
    if len(argv) != 2:
        print("Usage: strcmp.py <filename>")
        exit(1)


def get_array():
    with open(argv[1], "r") as f:
        return f.readline().strip().split(",")


def get_user_input(d):
    total = int(input("Enter number of arrays to compare: "))

    for i in range(total):
        d[f"{chr(97+i)}_hits"] = []
        d[chr(97+i)] = input(f"Enter array number {i+1} (comma-separated values): ").strip().split(",")
        for j in range(len(d[chr(97+i)])):
            d[f"{chr(97+i)}_hits"].append(False)


def parse_hits(d):
    # Parse hits
    for k, v in d.items():
        if k == "array":
            continue
        
        index = 0
        for s in v:
            if s in d["array"]:
                d[f"{k}_hits"][index] = True
            index += 1


def compare():
    to_compare = {}
    to_compare["array"] = get_array()
    get_user_input(to_compare)
    parse_hits(to_compare)
    
    for k, v in to_compare.items():
        score = 0
        
        if v[0] == True:
            for b in v:
                if b == True:
                    score += 1
        
        if score == len(v):
            print(f'All matches: {k}')


def main():
    check()
    compare()


if __name__ == '__main__':
    main()
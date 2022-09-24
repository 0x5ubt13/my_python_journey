import sys

names = ["Bill", "Charlie", "Fred", "George", "Ginny", "Percy", "Ron"]

# Linear search
if "Ron" in names:
    print("Found")
    sys.exit(0)

print("Not found")
sys.exit(1)
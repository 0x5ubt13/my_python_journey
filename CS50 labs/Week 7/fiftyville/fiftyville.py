from sys import argv
import sqlite3

def usage():
    """Show correct usage"""
    print("fiftyville.py <SQL query>")

def main():
    # If only 1 arg passed along the name of the program, print the first one
    if len(argv) == 2:
        with open("./log.sql", "w") as log:
            

            log.write(query)
            
    else:
        usage()
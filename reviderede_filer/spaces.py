'''Scopus Search String Prepare'''
#Prepares a string for quick insert into basic search

import csv
from sys import argv

INPUT_FILE = argv[1] #1st. argument containing name of input file.
OUTPUT_FILE = argv[2] #2nd. argument containing name of output file.

def open_file(file_name):
    with open(file_name, newline='') as _:
        reader = csv.reader(_, delimiter=';')
        #next(_)
        for row in reader:
            data = '"' + row[0] + '"' + ' OR  '
            write_file(OUTPUT_FILE, data)

def write_file(file_name, data):
    with open(file_name, mode="a") as file:
        file.write(data)

def main():
    """main"""
    open_file(INPUT_FILE)

if __name__ == '__main__':
    main()

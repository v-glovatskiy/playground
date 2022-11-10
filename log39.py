from sys import argv
import os

if len(argv) < 3:
    print('Fatal: you forgot to enter an argument.')

script, filename, second = argv

if not os.access(filename, os.F_OK):
    print('No such file')
txt = open(filename)

for row in txt:
    if "COMPLETED" in row:
        words = row.split()
        a = words[-1]
        c = float(a)
        b = float(second)
        if c > b:
            print(c)
           

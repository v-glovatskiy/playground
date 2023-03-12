
from sys import argv
import os
import csv

if len(argv) < 3:
    print('Fatal: you forgot to enter an argument.')

script, filename, second = argv
mame = second
a = []

if not os.access(filename, os.F_OK):
    print('No such file')
    os._exit(os.F_OK)

with open(filename, "r", newline="") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        if row["log_level"] == mame:
            a.append(mame)
print(len(a))
            
    
            
                                
    







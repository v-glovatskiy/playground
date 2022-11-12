from sys import argv
import os
from operator import itemgetter

if len(argv) < 2:
    print('Fatal: you forgot to enter an argument.')

script, filename = argv

if not os.access(filename, os.F_OK):
    print('No such file')

txt = open(filename)

for row in txt:
    if "COMPLETED" in row:
        if "Background::AllocationSendToTriage" in row:

            words = row.split()
            a = itemgetter(5,-1)(words)
            print(a)
           

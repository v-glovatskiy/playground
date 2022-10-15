
from sys import argv
import os

if len(argv) < 2:
    print('Fatal: you forgot to enter an argument.')
else:
    print('Argument exists')
script, filename = argv

name = 'COMPLETED after 1'
if os.access(filename, os.F_OK):
    print('Given file path is exist.')
else:
    print('No such file')


txt = open(filename)

print('File content %r' % filename)

for string in txt:
    if name in string:    
        print(string)
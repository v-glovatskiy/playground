from sys import argv
import os

if len(argv) < 3:
    print('Fatal: you forgot to enter an argument.')
else:
    print('Argument exists')
script, filename, second = argv
print(argv)

name = second
if os.access(filename, os.F_OK):
    print('Given file path is exist.')
else:
    print('No such file')


txt = open(filename)

print('File content %r' % filename)

for string in txt:
    words = string.split()
            
    for vav in words:
            
        if name in words:
            print(vav)
            

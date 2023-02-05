
from sys import argv
import os
import csv

if len(argv)<2:
    print ('Fatal: you forgot to enter an argument.')
else:
    print('argument exists')
script, filename = argv

name = 'ERROR'
if os.access((filename), os.F_OK): 
    print ('Given file path is exist.')

if os.access((filename), os.R_OK):
    print ('File is accessible to read')
 
if os.access((filename), os.W_OK): 
    print ('File is accessible to write')
 
else:
    print('no such file')


txt = open(filename)

print ('Содержимое файла %r' % filename)
#print (txt.read())

for string in txt:

    if name in string:
                   
        print(string)



    


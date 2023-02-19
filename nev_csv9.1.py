
from sys import argv
import os
import csv

if len(argv)<3:
    print ('Fatal: you forgot to enter an argument.')

script, filename, second = argv

second = 'ERROR'
if not os.access(filename, os.F_OK):
    print('No such file')
    os._exit(os.F_OK)

with open(filename,"r",newline="")as file:
	reader = csv.reader(file)
	for row in reader:
			if second in row:
			    print(row)



    


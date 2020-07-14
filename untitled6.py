nam = input('Enter your name:')
age = int(input('Enter the number:'))
print (nam) 
print(age)
f = (nam),(age)

import csv
 
with open('database.csv','a',newline='')as file:
	csv.writer(file).writerow(f)
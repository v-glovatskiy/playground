import csv

with open('example.csv') as file:
	reader = csv.reader(file,delimiter=',',quotechar=',',
                         quoting =csv.QUOTE_MINIMAL)
		
	for row in reader:
		print(row)
	

	
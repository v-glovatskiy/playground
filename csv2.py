import csv

FILENAME ="users.csv"

with open(FILENAME,"r",newline="")as file:
	reader = csv.reader(file)
	for row in reader:
		print(row[0],"-",row[1])
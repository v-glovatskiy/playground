import csv

with open('user1.csv') as f:
	reader =csv.DictReader(f)
	for row in reader:
		if int(row['money']) < 0:
		    print(row['user'])


import csv
name = 'ERROR'
with open('app_2023_jan.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        if name in row:
            print(row)
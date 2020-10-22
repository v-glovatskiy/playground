#импорт csv файла
import csv
# оглашение функции с параметром(csv_file)название параметраметра

def clean_csv(csv_file):
	#открытие и чтение 
	with open(filename, 'r') as csv_file:
		reader = csv.DictReader(csv_file,delimiter=',')
		result = []


	for raw in reader:
		if len(raw['level']) != 0 :
			result.append(raw)
			

		if len(raw['category']) !=0 :
			result.append(raw)

		if len(raw['skill']) !=0 :
			result.append(raw)

		if len(raw['rec_type']) !=0 :
			result.append(raw)

		if len(raw['rank']) !=0 :
			result.append(raw)

		if len(raw['recommendation_url']) !=0 :
			result.append(raw)

		if len(raw['short_desc']) !=0 :
			result.append(raw)	
			
	return result





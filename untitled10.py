import csv

# питамо операцію яку зробити
x = input('ведите число 1 или 2:')
x = int(x)

if x == 1:
	# спитати імя
	# спитати суму
	# зберегти імя і суму в файл
	name = input('enter your name:')
	money =int(input('enter the number:'))

	print (name)
	print (money)

	f = {'name': name, 'money': money}


	with open('database1.csv','a',newline='')as file:
		colums = ['name','money']

		writer = csv.DictWriter(file,fieldnames=colums)
		writer.writerow(f) 	
elif x == 2:
	# спитати імя
	# використати цикл for та надрукувати money з цим імям
	name = input('enter your name:')
	money = int(input('enter the number:'))
	with open('database1.csv','r')as file:
		reader = csv.DictReader(file)
		for i in reader:
			if i['name'] == name:
				row ={'name': name,'money':money}
				print (row)
					
				
else:
	# надрукувати помилку що неправильна операція
	print('неверная операция')

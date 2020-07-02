import pickle

FILENAME = "users.dat"

users = [
    ["Tom",28,True],
    ["Alise",23, False],
    ["Bob",34, False]
]    

with open(FILENAME,"wb")as file:
	pickle.dump(users,file)

with open(FILENAME,"rb") as file:
	users_from_file = pickle.load(file)
	for  user in users_from_file:
		print("Имя:",user[0],"\tВозраст:","\tЖенат(замужем):",user[2])


	




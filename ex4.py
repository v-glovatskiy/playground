cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven =cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car =passengers /cars_driven


print('в наличии',cars,'автомобилей')
print('только',drivers,'водителей вышли на работу')
print('поетому',cars_not_driven,'машин не работает')
print('мы можем сегодня перевезти',carpool_capacity,'человек')
print('сегодня нужно отвезти',passengers,'человек')
print('в каждой машине будет примерно',average_passengers_per_car,'человека'
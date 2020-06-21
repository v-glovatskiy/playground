#  калькулятор

what = input( "что делаем? (+,-,*,/,): ")

a = float( input( "введите первое число:"))
b = float( input( "введите второе число:"))

if what == "+":
	c = a + b	
	print( "результат: " + str(c))
elif what == "-":
	c = a - b 
	print( "результат: " + str(c))
elif what == "*": 
	c = a * b
	print( "результат: " + str(c))	 
elif what == "/":
    c = a / b
    print( "результат: " + str(c))
else :
	print( "выбрана неверная операция !")    



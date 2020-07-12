import calc

def test_add():
	if calc.add(1,2) == 3:
		print('test add(a,b) is OK')
	else:
	    print('test add(a,b) is Fail')

def  test_sub():
	if calc.sub(4,2) == 2:
		print('test sub()(a,b) is OK')
	else:
		print('test sub(a,b,) is Fail')

def  test_mul():
	if calc.mul(2,5) == 10:
		print('test mul(a,b) is OK')			
	else:
		print('test mul(a,b) is Fail')			

def  test_div():
	if calc.div(8,4) == 4:
		print('test div(a,b) is OK')
	else:
		print('test div(a,b) is Fail')

	
	

test_add()
test_sub()
test_mul()
test_div()
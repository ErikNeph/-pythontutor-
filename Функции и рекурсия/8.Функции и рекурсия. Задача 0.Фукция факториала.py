# Функция факториала 

def factorial(n):
	res = 1
	for i in range(1, n + 1):
		res *= i
	return res
	
print(factorial(3))
print(factorial(5))



'''def factorial_v2(n):
	res = 1
	for i in range(1, n + 1):
		res *= i
	return res

	
for i in range(1, 10):
	print(i, '! = ', factorial_v2(i), sep = '')'''

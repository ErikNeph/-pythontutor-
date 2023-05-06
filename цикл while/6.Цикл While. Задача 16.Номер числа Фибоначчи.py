# Условие
# Дано натуральное число A. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φn = A. 
# Если А не является числом Фибоначчи, выведите число -1.

x = 0
x1 = 1
x2 = 0
i = 0
n = int(input())
while x <= n:
	x = x1 + x2
	x1, x2 = x, x1
	i += 1
if (n == x2):
	print(i)
else:
	print(-1)		


'''a = int(input())
if a == 0:
	print(0)
else:
	fib_prev, fib_next = 0, 1
	n = 1
	while fib_next <= a:
		if fib_next == a:
			print(n)
			break
		fib_prev, fib_next = fib_next, fib_prev + fib_next
		n += 1
	else:
		print(-1)'''

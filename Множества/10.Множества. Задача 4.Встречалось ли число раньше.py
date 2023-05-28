# Условие
# Во входной строке записана последовательность чисел через пробел. Для
# каждого числа выведите слово YES (в отдельной строке), если это число ранее
# встречалось в последовательности или NO, если не встречалось.


numbers = [int(s) for s in input().split()]
occur_before = set()
for num in numbers:
	if num in occur_before:
		print('YES')
	else:
		print('NO')
		occur_before.add(num)
		
'''a = input().split()
for i in range(len(a)):
	if a[i] in a[:i]:
		print('YES')
	else:
		print('NO')


a = [int(num) for num in input().split()]

for i in range(len(a)):
	x = a[i]
	y = a[:i]
	if x in y:
		print('YES')
	else:
		print('NO')'''

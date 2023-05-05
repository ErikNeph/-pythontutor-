# Условие
# Последовательность состоит из различных натуральных чисел и завершается числом 0. Определите значение второго
# по величине элемента в этой последовательности. Гарантируется, что в последовательности есть хотя бы два элемента.

first_max = int(input())
second_max = int(input())
if first_max < second_max:
	first_max, second_max = second_max, first_max
element = int(input())
while element != 0:
	if element > first_max:
		second_max, first_max = first_max, element
	elif element > second_max:
		second_max = element
	element = int(input())
print(second_max)


'''a = int(input())
max1 = 0
max2 = 0
while a !=0:
	if a>max1:
		max2 = max1
		max1 = a
	elif a > max2:
		max2 = a
	a= int(input())
print(max2)'''

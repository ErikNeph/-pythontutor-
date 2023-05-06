# Условие
# Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите, сколько элементов этой последовательности равны ее наибольшему элементу.

max = 0
num_max = 0
element = -1
while element != 0:
	element = int(input())
	if element > max:
		max, num_max = element, 1
	elif element == max:
		num_max += 1
print(num_max)

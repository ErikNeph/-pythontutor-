# Условие
# Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите значение наибольшего элемента последовательности.

max = 0
element = -1
while element != 0:
	element = int(input())
	if element > max:
		max = element
print(max)

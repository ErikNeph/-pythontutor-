# Условие
# Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите, сколько элементов этой последовательности больше предыдущего элемента.

prev = int(input())
answer = 0
while prev != 0:
	next = int(input())
	if next != 0 and prev < next:
		answer += 1
	prev = next
print(answer)

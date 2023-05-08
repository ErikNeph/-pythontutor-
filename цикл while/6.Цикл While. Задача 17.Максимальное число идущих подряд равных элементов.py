# Условие
# Дана последовательность натуральных чисел, завершающаяся числом 0.
# Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу.

prev = -1
curr_len = 0
max_len = 0
element = int(input())
while element != 0:
	if prev == element:
		curr_len += 1
	else:
		prev = element
		max_len = max(max_len, curr_len)
		curr_len = 1
	element = int(input())
max_len = max(max_len, curr_len)
print(max_len)

# Условие
# Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.

a = [int(i) for i in input().split()]
num_distance = 1
for i in range(0, len(a) - 1):
	if a[i] != a[i + 1]:
		num_distance += 1
print(num_distance)

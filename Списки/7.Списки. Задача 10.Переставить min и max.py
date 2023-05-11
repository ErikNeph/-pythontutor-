# Условие
# В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.

a = [int(s) for s in input().split()]
min_element = 0
max_element = 0
for i in range(1, len(a)):
	if a[i] > a[max_element]:
		max_element = i
	if a[i] < a[min_element]:
		min_element = i
a[min_element], a[max_element] = a[max_element], a[min_element]
print(' '.join([str(i) for i in a]))

'''n = [int(i) for i in input().split()]
max = n.index(max(n))
min = n.index(min(n))
n[max], n[min] = n[min], n[max]
print(' '.join([str(i) for i in n]))'''

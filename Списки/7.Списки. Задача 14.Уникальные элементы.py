# Условие
# Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том
# порядке, в котором они встречаются в списке.

a = [int(s) for s in input().split()]
for i in range(len(a)):
	for q in range(len(a)):
		if i != q and a[i] == a[q]:
			break
	else:
		print(a[i], end = ' ')

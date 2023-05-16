# Условие
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8
# ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 — координаты 8 ферзей. Если ферзи не бьют
# друг друга, выведите слово NO, иначе выведите YES.


n = 8
x = []
y = []
for i in range(n):
	new_x, new_y = [int(s) for s in input().split()]
	x.append(new_x)
	y.append(new_y)

	
correct = True
for i in range(n):
	for q in range(i + 1, n):
		if x[i] == x[q] or y[i] == y[q] or abs(x[i] - x[q]) == abs(y[i] - y[q]):
			correct = False


if correct:
	print('NO')
else:
	print('YES')

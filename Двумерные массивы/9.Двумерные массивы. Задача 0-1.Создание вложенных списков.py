# Создание вложенных списков
# 3 Метода:

n = 3
m = 4
a = [0] * n
for i in range(n):
	a[i] = [0] * m
print(a)


a = 3
b = 4
a1 = []
for i in range(a):
	a1.append([0] * b)
print(a1)


# Топ вариант через генератор списка !
x = 3
y = 4
a2 = [[0] * y for i in range(x)]
print(a2)

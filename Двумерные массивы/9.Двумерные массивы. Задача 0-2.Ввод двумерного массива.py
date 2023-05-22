# Ввод двумерного массива
# 3 способа:


# в первой строке ввода идёт количество строк массива
n = int(input())
a = []
for i in range(n):
	a.append([int(q) for q in input().split()])
	

# в первой строке ввода идёт количество строк массива
n = int(input())
a = []
for i in range(n):
	row = input().split()
	for i in range(len(row)):
		row[i] = int(row[i])
	a.append(row)
	
	
# в первой строке ввода идёт количество строк массива
n = int(input())
a = [[int(q) for q in input().split()] for i in range(n)]
print(a)

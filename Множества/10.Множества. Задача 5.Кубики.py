# Условие
# Аня и Боря любят играть в разноцветные кубики, причем у каждого из них
# свой набор и в каждом наборе все кубики различны по цвету. Однажды дети
# заинтересовались, сколько существуют цветов таких, что кубики каждого цвета
# присутствуют в обоих наборах. Для этого они занумеровали все цвета
# случайными числами от 0 до 10 8 степени. На этом их энтузиазм иссяк, поэтому вам предлагается помочь им в оставшейся части.
# В первой строке входных данных записаны числа N и M — число кубиков у Ани и Бори. 
# В следующих N строках заданы номера цветов кубиков Ани. В последних M строках номера цветов Бори.
# Найдите три множества: номера цветов кубиков, которые есть в обоих
# наборах; номера цветов кубиков, которые есть только у Ани и номера цветов
# кубиков, которые есть только у Бори. Для каждого из множеств выведите
# сначала количество элементов в нем, а затем сами элементы, отсортированные по возрастанию.


def print_set(some_set):
    print(len(some_set))
    print(*[str(item) for item in sorted(some_set)])
 
N, M = [int(s) for s in input().split()]
A_colors, B_colors = set(), set()
for i in range(N):
    A_colors.add(int(input()))
for i in range(M):
    B_colors.add(int(input()))
     
print_set(A_colors & B_colors)
print_set(A_colors - B_colors)
print_set(B_colors - A_colors)


'''m, n = ([int(i) for i in input().split()])
a, b = set(), set()
for i in range(m):
	a.add(int(input()))
for i in range(n):
	b.add(int(input()))
print(len(a.intersection(b)))
print(*sorted(a.intersection(b)))
print(len(a.difference(b)))
print(*sorted(a.difference(b)))
print(len(b.difference(a)))
print(*sorted(b.difference(a)))'''

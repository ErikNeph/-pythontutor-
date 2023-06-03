# Условие
# Каждый из некоторого множества школьников некоторой школы знает некоторое количество языков. Нужно
# определить сколько языков знают все школьники, и сколько языков знает хотя бы один из школьников.
# В первой строке задано количество школьников. Для каждого из школьников сперва записано количество языков,
# которое он знает, а затем - названия языков, по одному в строке.
# В первой строке выведите количество языков, которые знают все школьники. Начиная со второй строки - список таких
# языков. Затем - количество языков, которые знает хотя бы один школьник, на следующих строках - список таких языков.
# Языки нужно выводить в лексикографическом порядке, по одному на строке.


students = [{input() for j in range(int(input()))} for i in range(int(input()))]
known_by_everyone, know_by_someone = set.intersection(*students), set.union(*students)
print(len(known_by_everyone), *sorted(known_by_everyone), sep = '\n')
print(len(know_by_someone), *sorted(know_by_someone), sep = '\n')


'''s = int(input())
mass=[]
for i in range(s):
    mass.append(set())
    for j in range(int(input())):
        mass[i].add(input())
evr = set.intersection(*mass)
all = set.union(*mass)
print(len(evr), *sorted(evr), sep='\n')
print(len(all), *sorted(all), sep='\n')'''

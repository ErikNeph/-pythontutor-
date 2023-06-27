# Условие
# В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель.
# Каждом элементу дерева сопоставляется целое неотрицательное число, называемое высотой. У родоначальника высота
# равна 0, у любого другого элемента высота на 1 больше, чем у его родителя.
# Вам дано генеалогическое древо, определите высоту всех его элементов.
# Программа получает на вход число элементов в генеалогическом древе N. Далее следует N−1 строка, задающие родителя
# для каждого элемента древа, кроме родоначальника. Каждая строка имеет вид имя_потомка имя_родителя.
# Программа должна вывести список всех элементов древа в лексикографическом порядке. После вывода имени каждого
# элемента необходимо вывести его высоту.
# Примечание
# Эта задача имеет решение сложности O(n), 
# но вам достаточно написать решение сложности O(n2) (не считая сложности обращения к элементам словаря).

def height(man):
    if man not in p_tree:
        return 0
    else:
        return 1 + height(p_tree[man])

p_tree = {}
n = int(input())
for i in range(n - 1):
    child, parent = input().split()
    p_tree[child] = parent

heights = {}
for man in set(p_tree.keys()).union(set(p_tree.values())):
    heights[man] = height(man)
    
for key, value in sorted(heights.items()):
    print(key, value)


'''n=int(input())
 
p_tree={}                                       #это будет словарь {ребёнок=родитель}
 
#создаём словарь p_tree
for _ in range (1,n):                         #читаем строки
    line=input()
    child,parent=line.split()                #ребёнок,родитель = 'str1 str2'.split()
    p_tree[child]=parent                    #p_tree[ребёнок]='родитель'
 
#all_man = множество, все люди 
all_man=set(p_tree.keys())|set(p_tree.values()) #(все имена в единственном числе) = (все родители) + (все дети)
 
heights={}                                      #будет словарь {предок=поколение}
 
#вычисляет поколение, попутно создаёт словарь, чтоб не вычислять одно и тоже
def f(name):                                 #передаём имя 
    if name not in p_tree:                #если нет родителя
        heights[name]=0                  #предок = 0,запись в словарь heights 
        return 0                                #значение поколения для дальнейшего вычисления
    parent=p_tree[name]                 #родитель = смотрим в (ребёнок=родитель)
    if parent in heights:                    #если известно поколение родителя
        value=heights[parent]+1         #поколение = (поколение родителя)+1
    else:
        value=f(parent)+1                  #поколение = поколение родителя +1, имя родителя отдаём функции, она вернёт поколение родителя
    heights[name]=value                  #добавляем в словарь heights нового предка [имя] = поколение
    return value                                #значение поколения для дальнейшего вычисления
 
#создадим словарь (предок=поколение)
for name in all_man:                         #возьмем всех по очереди
    if name not in heights:                  #берём только тех, кого нет в словаре (предок=поколение)
        f(name)                                   #дать имени поколение попутно создавая словарь (предок-поколение)
        
for name in sorted(heights):
    print(name,heights[name])
    
    
    
    
def height(x):
    #Эта функция будет рекурсивно вычислять уровень человека в дереве
    if x not in p_tree:
        return 0
    else:
        return 1 + height(p_tree[x])
    
p_tree = dict() #словарь ребенок -> родитель
N = int(input())
for i in range(N-1):
    child,parent = input().split()
    p_tree[child] = parent
    
heights = dict()
for x in set(p_tree).union(set(p_tree.values())):
    heights[x] = height(x)

for key in sorted(heights):
    print(key, heights[key])'''

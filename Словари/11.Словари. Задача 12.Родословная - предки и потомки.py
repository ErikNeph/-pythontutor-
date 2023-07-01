# Условие
# Даны два элемента в дереве. Определите, является ли один из них потомком другого.
# Во входных данных записано дерево в том же формате, что и в предыдущей задаче Далее идет число запросов K. В
# каждой из следующих K строк, содержатся имена двух элементов дерева.
# Для каждого такого запроса выведите одно из трех чисел: 1, если первый элемент является предком второго, 2, если
# второй является предком первого или 0, если ни один из них не является предком другого.
#9
#Alexei Peter_I
#Anna Peter_I
#Elizabeth Peter_I
#Peter_II Alexei
#Peter_III Anna
#Paul_I Peter_III
#Alexander_I Paul_I
#Nicholaus_I Paul_I
#3
#Alexander_I Nicholaus_I
#Peter_II Paul_I
#Alexander_I Anna

def is_ancestor(man, older_man):
    if man == older_man:
        return True
    while man in p_tree:
        man = p_tree[man]
        if man == older_man:
            return True
    return False

p_tree = dict()
n = int(input())
for i in range(n - 1):
    child, parent = input().split()
    p_tree[child] = parent
    
for i in range(int(input())):
    first, second = input().split()
    if is_ancestor(second, first):
        print(1, end = ' ')
    elif is_ancestor(first, second):
        print(2, end = ' ')
    else:
        print(0, end = ' ')


'''d = {}
for _ in range(int(input()) - 1):
    pot, predok = map(str, input().split())
    d[pot] = predok
for _ in range(int(input())):
    hum1, hum2 = map(str, input().split())
    p1, p2 = hum1, hum2
    s = 2
    while s != 0:
        if p1 in d:
            if d[p1] == hum2:
                break
            else:
                p1 = d[p1]
        else:
            hum1, hum2 = hum2, hum1
            p1, p2 = hum1, hum2
            s -= 1
    print(s, end=' ')'''

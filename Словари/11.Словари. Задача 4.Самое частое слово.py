# Условие
# Дан текст: в первой строке задано число строк, далее идут сами строки. Выведите слово, которое в этом тексте чаще
# встречается. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

counter = {}
for i in range(int(input())):
	line = input().split()
	for word in line:
		counter[word] = counter.get(word, 0) + 1
		
max_count = max(counter.values())
most_frequent = [k for k , v in counter.items() if v == max_count]
print(min(most_frequent))



'''n = int(input())
d = {}
for i in range(n):
    a = input().split()
    for b in a:
        d[b] = d.get(b, 0) + 1
m = max(d.values())
l = set()
for key in d:
    if d[key] == m:
        l.add(key)
print (sorted(l)[0])'''

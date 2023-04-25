# Условие
# Дана строка. Заменив в этой строке все появления буквы h на букву H, 
# кроме первого и последнего вхождения.

s = input()
a = s[:s.find('h') + 1] 
b = s[s.find('h') + 1:s.rfind('h')]
c = s[s.rfind('h'):]
s = a + b.replace('h', 'H') + c
print(s)

'''w = input()
w = w.replace('h', 'H', w.count('h') -1)
w = w.replace('H', 'h', 1)
print(w)'''

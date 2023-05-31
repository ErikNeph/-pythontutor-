# Условие
# Дан текст: в первой строке записано число строк, далее идут сами строки. 
# Определите, сколько различных слов содержится в этом тексте.
# Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим
# числом пробелов или символами конца строки.

words = set()
for i in range(int(input())):
	words.update(input().split())
print(len(words))


	
'''Count_of_strings = int(input())
List = []
for i in range(Count_of_strings):
    for element in input().split():
        List.append(element)
        
print(len(set(List)))'''

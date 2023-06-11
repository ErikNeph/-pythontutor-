# Условие
# В единственной строке записан текст. Для каждого слова из данного текста подсчитайте, 
# сколько раз оно встречалось в этом тексте ранее.
# Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим
# числом пробелов или символами конца строки.


counter = {}
for word in input().split():
	counter[word] = counter.get(word, 0) + 1
	print(counter[word] -1, end = ' ')


'''words = input().split()
dictionary = {}
for word in words:
	if word not in dictionary:
		dictionary[word] = 0
	else:
		dictionary[word] += 1
	print(dictionary[word])'''
	
	
#a={}
#for word in input().split():
    #if word in a:
        #a[word] = a.get(word)+1
        #print(a.get(word))
    #else:
        #a[word]=0
        #print(a.get(word))

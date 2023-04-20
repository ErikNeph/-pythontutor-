# Условие
# Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания, если A < B, или в
# порядке убывания в противном случае.

A, B = [int(input()) for i in range(2)]
if A < B:
	for i in range(A , B + 1):
		print(i)
else:
	for i in range(A, B - 1, -1):
		print(i)
	

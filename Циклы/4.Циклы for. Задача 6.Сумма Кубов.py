# Условие
# По данному натуральному n вычислите сумму 1в кубе3+2в кубе3+3в кубе3+...+nв кубе3.

n = int(input())
sum = 0
for i in range(n + 1):
	sum += i ** 3
print(sum) 

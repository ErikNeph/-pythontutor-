# Условие
# По данному натуральному числу N найдите наибольшую целую степень
# двойки, не превосходящую N. Выведите показатель степени и саму степень.
# Операцией возведения в степень пользоваться нельзя!

n = int(input())
two_in_pow = 2 
power = 1
while two_in_pow <= n:
	two_in_pow *= 2
	power += 1
print(power - 1, two_in_pow // 2)


'''n = int(input())
i = 1
while 2 ** i <= n:
	i += 1
print(i - 1, 2**(i - 1))'''

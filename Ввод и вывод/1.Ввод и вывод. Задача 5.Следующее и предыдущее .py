# Условие
# Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере
# (пробелы важны!).
# The next number for the number 1534 is 1535.
# The previous number for the number 1534 is 1533.

Number = int(input())
print('The next number for the number {0} is {1}.'.format(Number, Number + 1))
print('The previous number for the number {0} is {1}.'.format(Number, Number - 1))

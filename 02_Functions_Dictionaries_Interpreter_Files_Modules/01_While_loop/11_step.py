# Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу в строке, и после
# первого введенного нуля выводит сумму полученных на вход чисел.
#
# Sample Input 1:
#
# 5
# -3
# 8
# 4
# 0
# Sample Output 1:
#
# 14
# Sample Input 2:
#
# 0
# Sample Output 2:
#
# 0


sum = 0
num = None
while num != 0:
    num = int(input())
    sum += num

print(sum)
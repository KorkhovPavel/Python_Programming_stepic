# Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
# (число повторяется столько раз, чему равно). На вход программе передаётся неотрицательное целое число
# n — столько элементов последовательности должна отобразить программа. На выходе ожидается последовательность
# чисел, записанных через пробел в одну строку.
#
# Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.
#
# Sample Input:
#
# 7
# Sample Output:
#
# 1 2 2 3 3 3 4

num = int(input())
lst = []
for i in range(num + 1):
    if i == 0:
        continue
    else:
        for k in range(i):
            lst.append(i)
print(lst[:num])

# Напишите программу, которая считывает с клавиатуры два числа aa и bb, считает и выводит на консоль среднее
# арифметическое всех чисел из отрезка [a; b][a;b], которые кратны числу 33.
#
# В приведенном ниже примере среднее арифметическое считается для чисел на отрезке [-5; 12][−5;12]. Всего чисел,
# делящихся на 33, на этом отрезке 66: -3, 0, 3, 6, 9, 12−3,0,3,6,9,12. Их среднее арифметическое равно 4.54.5
#
# На вход программе подаются интервалы, внутри которых всегда есть хотя бы одно число, которое делится на 33.﻿
#
# Sample Input:
#
# -5
# 12
# Sample Output:
#
# 4.5
# i

a = int(input())
b = int(input())
sums = 0
counter = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        sum += i
        counter += 1
print(sums / counter)

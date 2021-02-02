# В то далёкое время, когда Паша ходил в школу, ему очень не нравилась формула Герона для вычисления площади
# треугольника, так как казалась слишком сложной. В один прекрасный момент Павел решил избавить всех школьников
# от страданий и написать и распространить по школам программу, вычисляющую площадь треугольника по трём сторонам.
#
# Одна проблема: так как эта формула не нравилась Павлу, он её не запомнил. Помогите ему завершить доброе дело и
# напишите
# программу, вычисляющую площадь треугольника по переданным длинам трёх его сторон по формуле Герона:
# а вход программе подаются целые числа, выводом программы должно являться вещественное число,
# соответствующее площади треугольника.

len_a = int(input())
len_b = int(input())
len_c = int(input())

p = (len_a + len_b + len_c) / 2
s = (p * (p - len_a) * (p - len_b) * (p - len_c)) ** 0.5
print(s)
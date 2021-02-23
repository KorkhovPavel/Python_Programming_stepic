# Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой:
#
# Требуется реализовать только функцию, решение не должно осуществлять операций ввода-вывода.
#
# Sample Input 1:
#
# 4.5
# Sample Output 1:
#
# 7.25
# Sample Input 2:
#
# -4.5
# Sample Output 2:
#
# -5.25
# Sample Input 3:
#
# 1
# Sample Output 3:
#
# -0.5


def f(x):
    # put your python code here
    if x <= -2:
        return 1 - (x + 2) ** 2
    elif -2 < x <= 2:
        return -x / 2
    elif 2 < x:
        return (x - 2) ** 2 + 1


print(f(1))

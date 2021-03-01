# Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке
# записана следующая информация:
#
# Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
#
# Поля внутри строки разделены точкой с запятой, оценки — целые числа.
#
# Напишите программу, которая считывает исходный файл с подобной структурой и для каждого абитуриента записывает
# его среднюю оценку по трём предметам на отдельной строке, соответствующей этому абитуриенту, в файл с ответом.
#
# Также вычислите средние баллы по математике, физике и русскому языку по всем абитуриентам и добавьте полученные
# значения, разделённые пробелом, последней строкой в файл с ответом.
#
# В качестве ответа на задание прикрепите полученный файл со средними оценками по каждому ученику и одной строкой
# со средними оценками по трём предметам.
#
# Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:
# print('First;Second-1 Second-2;Third'.split(';'))
# # ['First', 'Second-1 Second-2', 'Third']
#
# Sample Input:
#
# Петров;85;92;78
# Сидоров;100;88;94
# Иванов;58;72;85
# Sample Output:
#
# 85.0
# 94.0
# 71.666666667
# 81.0 84.0 85.666666667

d = {}
num = 0
mat = 0
fiz = 0
rus = 0
count = 0
with open('dataset_3363_4.txt') as ff:
    for i in ff:
        count += 1
        for v in i.split():
            for k, f in enumerate(v.split(';')):
                if f.isdigit():
                    num += int(f)

                    if k == 1:
                        mat += int(f)
                    elif k == 2:
                        fiz += int(f)
                    elif k == 3:
                        rus += int(f)

            r = open('data.txt', 'a')
            r.write(f'{num / 3}\n')
            num = 0
r.write(f'{mat / count} {fiz / count} {rus / count}\n')
r.close()
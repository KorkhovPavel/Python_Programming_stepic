# Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и
# выводит на стандартный вывод сводную таблицу результатов всех матчей.
#
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
#
# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
#
# Вывод программы необходимо оформить следующим образом:
# Команда:Всего_игр Побед Ничьих Поражений Всего_очков
#
# Конкретный пример ввода-вывода приведён ниже.
#
# Порядок вывода команд произвольный.
#
# Sample Input:
#
# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
# Sample Output:
#
# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6

# put your python code here

num_game = int(input())
d = {}
for i in range(num_game):
    item = input().split(';')
    for v in [item[0], item[2]]:
        if v not in d:
            d[v] = [1, 0, 0, 0, 0]
        else:
            d[v][0] += 1

    if int(item[1]) > int(item[3]):
        d[item[0]][1] += 1
        d[item[2]][3] += 1
        d[item[0]][4] += 3

    elif int(item[1]) < int(item[3]):
        d[item[2]][1] += 1
        d[item[0]][3] += 1
        d[item[2]][4] += 3

    elif int(item[1]) == int(item[3]):
        d[item[0]][2] += 1
        d[item[2]][2] += 1
        d[item[2]][4] += 1
        d[item[0]][4] += 1

for k, v in d.items():
    print(f'{k}:{v[0]} {v[1]} {v[2]} {v[3]} {v[4]}')
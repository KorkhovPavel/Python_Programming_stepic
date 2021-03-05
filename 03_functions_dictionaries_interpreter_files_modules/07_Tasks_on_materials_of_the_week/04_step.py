# Группа биологов в институте биоинформатики завела себе черепашку.
#
# После дрессировки черепашка научилась понимать и запоминать указания биологов следующего вида:
# север 10
# запад 20
# юг 30
# восток 40
# где первое слово — это направление, в котором должна двигаться черепашка, а число после слова — это положительное
# расстояние в сантиметрах, которое должна пройти черепашка.
#
# Но команды даются быстро, а черепашка ползёт медленно, и программисты догадались, что можно написать программу,
# которая определит, куда в итоге биологи приведут черепашку. Для этого программисты просят вас написать программу,
# которая выведет точку, в которой окажется черепашка после всех команд. Для простоты они решили считать, что движение
# начинается в точке (0, 0), и движение на восток увеличивает первую координату, а на север — вторую.
#
# Программе подаётся на вход число команд nn, которые нужно выполнить черепашке, после чего nn строк с самими командами.
# Вывести нужно два числа в одну строку: первую и вторую координату конечной точки черепашки.
# Все координаты целочисленные.
#
# Sample Input:
#
# 4
# север 10
# запад 20
# юг 30
# восток 40
# Sample Output:
#
# 20 -20
# put your python code here
num = int(input())
x = 0
y = 0
xy = 0
for i in range(num):
    item = input().split()
    for v in item:
        if v.isdigit():
            xy = int(v)
    if 'север' in item:
        y += xy
    elif 'запад' in item:
        x -= xy
    elif 'юг' in item:
        y -= xy
    elif 'восток' in item:
        x += xy

print(x, y)

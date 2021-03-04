# Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
# Если введённое слово не найдено в этом списке, оно помечается как "ошибка".
#
# Попробуем написать подобную систему.
#
# На вход программе первой строкой передаётся количество dd известных нам слов, после чего на dd строках
# указываются эти слова. Затем передаётся количество ll строк текста для проверки, после чего ll строк текста.
#
# Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.
#
# Sample Input:
#
# 4
# champions
# we
# are
# Stepik
# 3
# We are the champignons
# We Are The Champions
# Stepic
# Sample Output:
#
# stepic
# champignons
# the


num = int(input())
lst = []
for i in range(num):
    val = input()
    lst.append(val)

finish_lis = []
num_1 = int(input())
for i in range(num_1):
    val = input().split(' ')
    for v in val:
        if v.lower() in [q.lower() for q in lst]:
            continue
        else:
            if v.lower() not in [q.lower() for q in finish_lis]:
                finish_lis.append(v)

for i in finish_lis:
    print(i)

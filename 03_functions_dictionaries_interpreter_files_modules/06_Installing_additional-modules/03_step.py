# Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
# Первое слово в тексте последнего файла: "We".
#
# Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
#
# Все файлы располагаются в каталоге по адресу:
# https://stepic.org/media/attachments/course67/3.6.3/
#
# Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.

import requests

urls = 'https://stepic.org/media/attachments/course67/3.6.3/'

with open('dataset_3378_3.txt') as ff:
    url = ff.read().strip()
    print(urls)
    res = requests.get(url)
    while True:
        res = requests.get(urls + res.text)
        if res:
            print(urls + res.text)
        else:
            break

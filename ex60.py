# имя проекта: python exercises
# номер версии: 1.0
# имя файла: ex60.py
# автор и его учебная группа: Э.Финце, ЭУ-120
# дата создания: 29.11.2019
# дата последней модификации: 24.12.2019
# связанные файлы:
# описание: Заданы M строк символов, которые вводятся с клавиатуры.
# Каждая строка представляет собой последовательность символов, включающих в себя вопросительные знаки.
# Заменить в каждой строке все имеющиеся вопросительные знаки звёздочками.
# версия Python: 3.7

import re

M = 3

list_strings = []

for i in range(0, M):
    print("Введите строку:", end=' ')
    list_strings.append(input())

for string in list_strings:
    string = re.sub(r'\?', '*', string)
    print(string)
# имя проекта: python exercises
# номер версии: 1.0
# имя файла: ex55.py
# автор и его учебная группа: Э.Финце, ЭУ-120
# дата создания: 29.11.2019
# дата последней модификации: 24.12.2019
# связанные файлы:
# описание: Заданы M строк слов, которые вводятся с клавиатуры (в каждой строке – одно слово).
# Вводится слог (последовательность букв). Удалить данный слог из каждой строки.
# версия Python: 3.7

import re

M = 3

list_strings = []

for i in range(0, M):
    print("Введите строку:", end=' ')
    list_strings.append(input())

print("Введите слог:", end=' ')
syllable = input()

for string in list_strings:
    string = re.sub(syllable, '', string)
    print(string)

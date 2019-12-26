# имя проекта: python exercises
# номер версии: 1.0
# имя файла: ex56.py
# автор и его учебная группа: Э.Финце, ЭУ-120
# дата создания: 29.11.2019
# дата последней модификации: 24.12.2019
# связанные файлы:
# описание: Заданы M строк символов, которые вводятся с клавиатуры.
# Напечатать все центральные буквы строк нечетной длины.
# версия Python: 3.7

import math

M = 3

list_strings = []

for i in range(0, M):
    print("Введите строку:", end=' ')
    list_strings.append(input())

for string in list_strings:
    strlen = len(string)

    if strlen % 2 != 0:
        print(string[math.ceil(strlen/2) - 1])

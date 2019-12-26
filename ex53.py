# имя проекта: python exercises
# номер версии: 1.0
# имя файла: ex53.py
# автор и его учебная группа: Э.Финце, ЭУ-120
# дата создания: 29.11.2019
# дата последней модификации: 24.12.2019
# связанные файлы:
# описание: Заданы M строк слов, которые вводятся с клавиатуры.
# Подсчитать количество гласных букв в каждой из заданных строк.
# версия Python: 3.7

import re

M = 4

def get_count(str):
    vowel = 0
    consonant = 0

    str = re.sub(r'\d', '', str)
    str = re.sub(r'\W', '', str)

    i = 0
    while i < len(str):
        char = str[i]
        if char.lower() in ['a', 'e', 'i', 'o', 'u', 'y',
                            'а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']:
            vowel += 1
        else:
            consonant += 1

        i += 1

    return vowel, consonant


list_strings = []

for i in range(0, M):
    print("Введите строку:", end=' ')
    list_strings.append(input())

for str in list_strings:
    vowel, consonant = get_count(str)
    print("В строке %s %s гласных и %s согласных" % (str, vowel, consonant))

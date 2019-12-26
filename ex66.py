# имя проекта: python exercises
# номер версии: 1.0
# имя файла: ex66.py
# автор и его учебная группа: Э.Финце, ЭУ-120
# дата создания: 29.11.2019
# дата последней модификации: 24.12.2019
# связанные файлы:
# описание: Для вводимых чисел определить процент положительных и отрицательных чисел.
# При вводе числа −65432 закончить работу.
# версия Python: 3.7

import re

list_numbers = []

count_positive = 0
count_negative = 0

while True:
    print("Введите число:", end=' ')
    string = re.sub(r'[^0-9\-]+', '', input())
    if len(string) == 0:
        print("В строке не обнаружено числа")
        continue

    number = int(string)

    if number * -1 == 65432:
        break

    list_numbers.append(number)

    if number < 0:
        count_negative += 1
    else:
        count_positive += 1


one_percent = 100 / len(list_numbers)
print("Процент положительных чисел:", one_percent * count_positive)
print("Процент отрицательных чисел:", one_percent * count_negative)

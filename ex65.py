# имя проекта: python exercises
# номер версии: 1.0
# имя файла: ex65.py
# автор и его учебная группа: Э.Финце, ЭУ-120
# дата создания: 29.11.2019
# дата последней модификации: 24.12.2019
# связанные файлы:
# описание: Вводятся положительные числа. Определить сумму чисел,
# делящихся на положительное число B нацело. При вводе отрицательного числа закончить работу.
# версия Python: 3.7

import re

list_numbers = []

B = 5
sum = 0

while True:
    print("Введите число:", end=' ')
    string = re.sub(r'[^0-9\-]+', '', input())
    if len(string) == 0:
        print("В строке не обнаружено числа")
        continue

    number = int(string)
    list_numbers.append(number)

    if number < 0:
        break

    if number % B == 0:
        sum += number

print("Сумма:", sum)

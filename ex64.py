# имя проекта: python exercises
# номер версии: 1.0
# имя файла: ex64.py
# автор и его учебная группа: Э.Финце, ЭУ-120
# дата создания: 29.11.2019
# дата последней модификации: 24.12.2019
# связанные файлы:
# описание: Суммировать вводимые числа, среди которых нет нулевых.
# При вводе нуля обеспечить вывод текущего значения суммы. При вводе числа 99999 закончить работу.
# версия Python: 3.7

import re

list_numbers = []

sum = 0


while True:
    print("Введите число:", end=' ')
    string = re.sub(r'[^0-9\-]+', '', input())
    if len(string) == 0:
        print("В строке не обнаружено числа")
        continue

    number = int(string)
    list_numbers.append(number)

    if number == 99999:
        break
    elif number == 0:
        print("Сумма:", sum)
    else:
        sum += number

print("Сумма:", sum)

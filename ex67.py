# имя проекта: python exercises
# номер версии: 1.0
# имя файла: ex67.py
# автор и его учебная группа: Э.Финце, ЭУ-120
# дата создания: 29.11.2019
# дата последней модификации: 24.12.2019
# связанные файлы:
# описание: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами.
# Найти наибольший элемент столбца матрицы A, для которого сумма абсолютных значений элементов максимальна.
# версия Python: 3.7

import random

N = 2
M = 3


def get_row(column):
    col = []
    for i in range(0, column):
        col.append(random.randint(0, 9))

    return col


def get_matrix(row, column):
    matrix = []
    for i in range(0, row):
        matrix.append(get_row(column))

    return matrix


def listsum(list):
    sum = 0
    for element in list:
        sum += element

    return sum


def print_matrix(matrix):
    i = 0
    while i < len(matrix):
        j = 0
        row = matrix[i]
        while j < len(row):
            column = row[j]
            print(column, end=' ')
            j += 1

        print()
        i += 1


A = get_matrix(N, M)

tmp = list(zip(*A))

max_sum = 0
index_column_max_sum = 0

i = 0
while i < len(tmp):
    column = tmp[i]
    current_list_sum = listsum(column)
    if current_list_sum > max_sum:
        max_sum = current_list_sum
        index_column_max_sum = i

    i += 1

print("Матрица:")
print_matrix(A)
print("Cтолбец для которого сумма абсолютных значений элементов максимальна:",
      index_column_max_sum)
print("Наибольший элемент этого столбца:", max(tmp[index_column_max_sum]))
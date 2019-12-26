# имя проекта: python exercises
# номер версии: 1.0
# имя файла: ex75.py
# автор и его учебная группа: Э.Финце, ЭУ-120
# дата создания: 29.11.2019
# дата последней модификации: 24.12.2019
# связанные файлы:
# описание: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами.
# Определить, сколько нулевых элементов содержится в верхних L строках матрицы и в левых К столбцах матрицы.
# версия Python: 3.7

import random

N = 5  
M = 7  

L = 3
K = 2


def get_row(column):
    col = []
    for i in range(0, column):
        col.append(random.randint(-9, 9))

    return col


def get_matrix(row, column):
    matrix = []
    for i in range(0, row):
        matrix.append(get_row(column))

    return matrix


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
print("Исходная матрица:")
print_matrix(A)

l_zeros = 0
k_zeros = 0


i = 0
while i < len(A):
    j = 0

    while j < len(A[i]):
        if A[i][j] == 0:
            if i < L:
                l_zeros += 1

            if j < K:
                k_zeros += 1
        j += 1

    i += 1

print("В верхних %s строках содержится %s нулей" % (L, l_zeros))
print("В левых %s столбцах содержится %s нулей" % (K, k_zeros))

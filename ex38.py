# Дан одномерный массив числовых значений, насчитывающий N элементов.
# Исключить из него M элементов, начиная с позиции K.

import numpy as np
import array
import random

N = int(input("Введите количество элементов массива "))
K = int(input("Позиция K "))
M = int(input("количество элементов для вычитания "))
A = [random.randint(0, 100) for i in range(0, N)]
print(A)

A.insert(K,M)
print(A)

A.delete(K,M)
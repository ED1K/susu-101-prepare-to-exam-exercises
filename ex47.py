# Дан одномерный массив числовых значений, насчитывающий N элементов.
# Исключить из массива элементы, принадлежащие промежутку [B; C].

import random
import numpy

N = int(input("Количество элементов массива "))
B = int(input("Элемент массива 1 "))
C = int(input("Элемент массива 2 "))
A = [random.randint(-10, 10) for i in range(0, N)]
print(A)

C = C + 1
del A[B:C]
print(A)


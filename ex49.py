# Дан одномерный массив числовых значений, насчитывающий N элементов.
# Определить, имеются ли в массиве два подряд идущих нуля.

import random
import numpy

N = int(input("Количество элементов в массиве "))
A = [random.randint(-1, 1) for i in range(0, N)]
print(A)

for i in range(N):
    if A[i] == 0 and A[i-1] == 0:
        print("Два подряд нуля в ",i-1," и ",i)

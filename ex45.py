# Дан одномерный массив числовых значений, насчитывающий N элементов. Добавить к элементам массива такой новый элемент,
# чтобы сумма элементов с положительными значениями стала бы равна
# модулю суммы элементов с отрицательными значениями.

import random
import numpy as np

N = int(input("Количество элементов массива "))
A = [random.randint(-10,10) for i in range(0,N)]
print(A)
Ao = []
Ap = []


for i in range(N):
    if A[i] > 0:
        Ap.append(A[i])
    if A[i] < 0:
        Ao.append(A[i])

sumAo = np.sum(Ao)
sumAp = np.sum(Ap)
sumAo = abs(sumAo)
Q = (sumAo-sumAp)
print(sumAo)
print(sumAp)
print(Q)

if sumAo == sumAp:
    print("Сумма отрицательных и положительных элементов массива равно")
if sumAo > sumAp:
    A.append([Q])
if sumAp > sumAo:
    A.append([Q])

print(A)

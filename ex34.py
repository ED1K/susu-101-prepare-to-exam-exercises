# Дан одномерный массив числовых значений, насчитывающий N элементов. Поменять местами первую и вторую половины массива.
import random

N = int(input("Введите количество элементов массива "))
a = [random.randint(0, 100) for i in range(0, N)]
print(a)

if (len(a) % 2 == 1):
    end = N
else:
    end = N-1


for i in range(end-1 // 2):
    a[i], a[i + end-1 // 2] = a[i + end-1 // 2], a[i]
print(a)
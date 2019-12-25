# Дан одномерный массив числовых значений, насчитывающий N элементов.
# Исключить все нулевые элементы.
import random
N = int(input("Введите количество элементов массива "))
A = [random.randint(-1, 1) for i in range(0, N)]
print(A)

B = filter(bool, A)
print(list(B))

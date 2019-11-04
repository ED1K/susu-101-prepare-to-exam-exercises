# Имеются две ёмкости: кубическая с ребром A, цилиндрическая с высотой H и радиусом основания R.
# Определить, поместится ли жидкость объёма M в первую ёмкость, во вторую, в обе.
import math
A = int(input("Ребро кубической ёмкости "))
R = int(input("Радиус основания цилиндрической ёмкости "))
H = int(input("Высота цилиндрической ёмкости "))
M = int(input("Объем жидкости "))

Sk = math.pow(A, 3)
print(Sk, "Объем куба")
Sc = ((math.pi) * (math.pow(R, 2)) * H)
print(Sc, "Объем цилиндра")
if (Sk + Sc > M ):
    print("Жидкость поместится в оба сосуда")
if (Sk >= M):
    print("Жидкость поместится в куб")
if (Sc >= M):
    print("Жидкость поместится в цилиндр")

import math

side_a = input("Введите длину стороны 1 ")
a = int(side_a)
side_b = input("Введите длину стороны 2 ")
b = int(side_b)
side_c = input("Введите длину стороны 3 ")
c = int(side_c)

if c>a+b or b>a+c or a>b+c:
    print("Треугольник с такими тсоронами не существует, проверьте данные")
else:
    p = a+b+c
    hp = p/2
    S = math.sqrt(hp*(hp-a)*(hp-b)*(hp-c))
    print("Периметр равен ", p)
    print("Площадь равна", S)
nx = input("Введите число x ")
nx = int(nx)
ny = input("Введите число y ")
ny = int(ny)

if nx == 0 or ny == 0:
    print("Значения не должны быть равны 0, проверьте данные")
else: Z = 1/(nx*ny)
print("Значение функции = ",Z)

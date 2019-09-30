num = input("Введите число для проверки ", )
num = int(num)

if num % 2 == 1 and num % 5 == 0:
    print("Число ",num, " нечетно и кратно 5")
else:
    print("Число не соответствует условию")

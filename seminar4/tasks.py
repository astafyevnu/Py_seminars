# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

# n = input("Input nimber: ").split()

# nmin = int(n[0])
# nmax = int(n[0])

# for i in n:
#     k = int(i)
#     if k > nmax:
#         nmax = k
#     if k < nmin:
#         nmin = k
# print(nmin, nmax)


# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:

#     1. с помощью математических формул нахождения корней квадратного уравнения


# a = int(input("Input nimber a: "))
# b = int(input("Input nimber b: "))
# c = int(input("Input nimber c: "))

# d = b ** 2 - 4 * a * c

# print("D = ", d)
# if d < 0:
#     print('No roots')
# elif d > 0:
#     print("two roots")
#     print("X1 = ", (-b + d ** 1 / 2) / 2 * a)
#     print("X2 = ", (-b - d ** 1 / 2) / 2 * a)
# else:
#     print('One roots')
#     print("X1 = ", (-b + d ** 1 / 2) / 2 * a)

#     2. с помощью дополнительных библиотек Python


# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.


x, y = 5, 3
n = max(x, y)

while True:
    if n % x == 0 and n % y == 0:
        i = n
        break
    n += 1
print(f'{i = }')
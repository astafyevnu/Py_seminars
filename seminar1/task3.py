# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

#     *Примеры:*

#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# 1
# n = int(input("input n: "))
# for i in range(-n, n +1):
#     print(i, end = ", ")

# 2
# n = int(input("input n: "))
# print(*range(-n, n + 1))

# 3
# n = int(input("input n: "))
# print(*range(-n, n + 1), sep = ", ")

# 4
print(*range(-(n := int(input("input n: "))), n + 1), sep=", ")

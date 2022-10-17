#     3. Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
# Пример:
# 1 -> 2.0
# 2 -> 4.25
# 3 -> 6.62037037037037

import math

n = int(input("input number N: "))
lst = []
sum = 0
for i in range(1, n+1):
    f_num = float((1 + 1 / i) ** i)
    lst.append(float(f_num))
print(math.fsum(lst))

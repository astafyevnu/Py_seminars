#     1. Вычислить число c заданной точностью d

#  Пример:

#         ◦ при d = 0.001, π = 3.142 10^(-1) ≤ d ≤10^(-10)

# way1
# import random

# n = random.uniform(1, 5)
# degree = random.randint(-10, -1)

# d = 10 ** degree
# result = round(n, -degree)
# print(f'Число {n} с точностью округления {d} равно {result}.')

# way2

from decimal import Decimal


n = input("input number: ")
d = input("round up to: ")

degree = '1.' + "0"*int(d)

num = Decimal(n)
result = num.quantize(Decimal(str(degree)))
print('result = ', result)

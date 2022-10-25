#     4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

#  Пример:

#         ◦ k=2 => 2x^2 + 4x + 5 = 0 или x^2 + 5 = 0 или 10x = 0

import random

k = int(input("Input degree k: "))
lst = []

def rnd():
    return random.randint(0, 100)


for i in range(k, 1, -1):
    c = rnd()
    if c:
        lst.append(f'{c}x^{i}')

c = rnd()
if c:
    lst.append(f'{c}x')
c = rnd()
if c:
    lst.append(f'{c}')

res = ' + '.join(lst) + ' = 0'

print(res)
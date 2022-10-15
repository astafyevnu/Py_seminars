#     2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.

#  Пример:

#         ◦ Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# way1
# num = int(input("input number N: "))

# d = {i: 3*i + 1 for i in range(1, num+1)}
# print(f"Итоговая последовательность: {d}")

# way2
# num = int(input("input number N: "))

# dct = {}
# for i in range(1, num+1):
#     dct[i] = 3 * i + 1

# print(f"Для n = {num}: ", dct)

# way3
 
print({i: 3*i+1 for i in range(1, (int(input("input number N: ")))+1)})
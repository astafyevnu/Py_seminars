#     2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#  Пример:

#         ◦ [2, 3, 4, 5, 6] => [12, 15, 16];
#         ◦ [2, 3, 5, 6] => [12, 15]

# lst = [2, 3, 4, 5, 6]
lst = [2, 3, 5, 6]

new_lst = []

count = len(lst)
for i in range(len(lst)):
    while i < len(lst)/2 and count > len(lst)/2:
        count -= 1
        n = lst[i] * lst[count]
        new_lst.append(n)
        i += 1
print(new_lst)

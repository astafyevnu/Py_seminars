#     3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

#  Пример:

#         ◦ [1.1, 1.2, 3.1, 5, 10.01] => 0.2

lst = [1.1, 1.2, 3.1, 5, 10.01]

min = 1
max = 0

for i in lst:
    tail = i - int(i)
    if tail <= min:
        min = tail
    if tail >= max:
        max = tail

print(round(max-min, 2))

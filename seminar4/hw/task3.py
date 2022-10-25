# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


from random import randint
lst = [randint(0, 20) for i in range(30)]
print(lst)

n_lst = [i for i in lst if lst.count(i) == 1]
print(n_lst)

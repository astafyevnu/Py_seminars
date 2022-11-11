# Урок 3. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension

# def f(x):
#     return x*x

# lst = [degree(i) for i in range(1, 21) if i % 2 == 0]
# print(lst)


# def f(x):
#     return x*x

# lst = [(i,
# f(i)) for i in range(1, 21) if i % 2 == 0]
# print(lst)


# nums = 'nums.txt'


# def read_nums(file):
#     with open(str(file), 'r') as data:
#         pol = data.read()
#     return pol


# def f(x):
#     return x*x

# lst = [(i,
# f(i)) for i in range(1, 21) if i % 2 == 0]
# print(lst)


# func map

# lst = [x for x in range(1, 20)]

# lst = list(map(lambda x:x+10, lst))

# print(lst)


#  in numbers

# data = map(int, '1 2 3 4 55 6'.split())

# for e in data:
#     print(e)


# func filter

# data = [x for x in range(10)]

# res = list(filter(lambda x: not x%2, data))
# print(res)


# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)


# func zip

# u = ['user1', 'user2', 'user3', 'user4', 'user5' ]

# ids = [4, 5, 9, 14, 7]

# data = list(zip(u, ids))

# print(data)


# u = ['user1', 'user2', 'user3', 'user4', 'user5' ]

# ids = [4, 5, 9, 14, 7]

# salary = [111, 222, 333]

# data = list(zip(u, ids, salary))

# print(data)


# func enumerate

# u = ['user1', 'user2', 'user3', 'user4', 'user5' ]

# ids = [4, 5, 9, 14, 7]

# data = list(enumerate(u))

# print(data)


# практика


#     1. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.


# with open ('task1.txt', 'r', encoding='utf-8') as f:
#     lst = f.read().split()
# print(lst)
# lst.sort()
# for i in range(1, len(lst)):
#     if int(lst[i]) - 1 != int(lst[i-1]):
#         print(f'Not found {int(lst[i])-1}.')
#         break


#     2. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.

#  Пример:

#  [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

# lst = [1, 5, 2, 3, 4, 6, 1, 7]

# if lst[0] +1 not in lst:
#     lst.remove(lst[0])
# res = [lst[0]]

# for i in lst:
#     if i > res[-1]:
#         res.append(i)
# print(res)
# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

# lst = ['swdfjh434', 'dds3', 'werfg355', 'weaffg34552fd', 'fdqw34', '3434dfdf']

# n = input('Введите искомое: ')

# for i in lst:
#     if n in i:
#         print("Да есть")
#         break
# else:
#     print("Отсутствует")

# way2
# lst = ['swdfjh434', 'dds3', 'werfg355', 'weaffg34552fd', 'fdqw34', '3434dfdf']
# n = input('Введите искомое: ')
# print('Yes' if n in ''.join(lst) else 'No')





# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

lst = ['swdfjh434', 'dds3', 'werfg355', 'weaffg34552fd', 'fdqw34', '3434dfdf', 'weaffg34552fd', 'dds3']
n = input('Введите искомое: ')
if n in lst:
    count = lst.index(n)
    for i in range(count+1, len(lst)):
        if lst[i] == count:
            print(i)
            break
    else:
        print(-1)
else:
    print(-1)
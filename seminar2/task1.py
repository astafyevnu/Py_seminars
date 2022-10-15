#     1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

#  Пример:

#         ◦ Для N = 5: 1, -3, 9, -27, 81

# way1

# num = int(input("input number N: "))

# for i in range(num):
#     print((-3) ** i, end=', ')


# way2

# num = int(input("input number N: "))
# lst = [1]
# for i in range(num-1):
#     lst.append(lst[i]*(-3))
# print(*lst, sep=', ')

 # way3
 
print(*((-3) ** i for i in range(int(input("input number N: ")))), sep=', ')
#     5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

#  Пример:

#         ◦ для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

k = int(input('Input number: '))

fib = [1, 1]
fibon = [1, -1]


for i in range(2, k):
    lst = fib[i-1]+fib[i-2]
    fib.append(lst)
    sub = fibon[i-2] - fibon[i-1]
    fibon.append(sub)

fibon.reverse()
fibon.append(0)

print(fibon+fib)

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input("input number: "))

# n = 2310

lst = []
num = n
i = 2

while i * i <= n:
    while num % i == 0:
        num //= i
        lst.append(i)
        
    i += 1

print(f"Cписок простых множителей числа: {set(lst)}")

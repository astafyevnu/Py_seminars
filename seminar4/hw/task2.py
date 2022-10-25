# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input("input number: "))

lst = []

i = 2

while i * i <= n:
    while n % i == 0:
        n //= i
        lst.append(i)
    i += 1

print(f"Cписок простых множителей числа: {set(lst)}" if len(
    lst) > 1 else "Число делится само на себя.")

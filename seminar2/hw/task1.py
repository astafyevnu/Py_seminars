#     1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

str_num = input("input number: ")
chars = ' -.,!'
new_str = str_num.translate(str.maketrans('', '', chars))
nums_sum = sum(int(x) for x in new_str)
print("Sum digits of number: ", nums_sum)

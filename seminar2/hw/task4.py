# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
import random

n = int(input("input number: "))
lst = random.sample(range(-n, n), n)

sum = 1
new_lst = []

with open('file.txt', 'r') as f:
    for i in f:
        if -len(lst) <= int(i) < len(lst):
            sum*= lst[int(i)]
            new_lst.append(lst[int(i)])

print("Sum new list: ", sum if sum != 1 else "Value not found")
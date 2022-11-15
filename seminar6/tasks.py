# Вычислить обратную польскую запись. Вычислите значение арифметического выражения в обратной польской записи. Допустимые операторы +, -, * и /.
# Каждый операнд может быть целым числом или другим выражением. Обратите внимание,
# что деление между двумя целыми числами должно усекаться до нуля. Числа в стеке всегда округляем до целых
# ["2","1","+","3","*"] -> 9 Пример: (3 * (2 + 1)) = 9


# ???

# ops = {
# "+": lambda a,b: a+b,
# "-": lambda a,b: a-b,
# "*": lambda a,b: a*b,
# "/": lambda a,b: a/b
# }

# def calculate(expr):
#     while '(' in expr:
#         pass

#     for ch in expr:
#         if ch.isdigit() or ch == '.':


#             source = ["2","1","+", "3", "*"]
#             result = []
#             for el in source:
#                 if el.isdigit():
#                     result.append(int(el))
#                 else:
#                     frst = result.pop()
#                     scnd = result.pop()
#                     result.append(ops[el](scnd, frst))
#             print(*result)


# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.

#  Пример:

#  2+2 => 4;

#  1+2*3 => 7;

#  1-2*3 => -5;


# Добавьте возможность использования скобок, меняющих приоритет операций.

#  Пример:

#  1+2*3 => 7;

#  (1+2)*3 => 9;

# from decimal import Decimal

# def create_lists(expr):
#     # while '(' in expr:
#     #     pass

#     num = ''
#     op = ''

#     for ch in expr:
#         if ch.isdigit() or ch == '.':
#             num+=ch
#         elif ch == '-':
#             num += ' ' + ch
#             op += '+'
#         elif ch == ' ':
#             continue
#         else:
#             ch += ch
#             num+= ' '

#     num, ex = list(map(Decimal, num.split())), list(op)


#     def make_operation(sign:str):
#         sign_index = op.index()
#         first_num = num[sign_index]
#         second_num = num[sign_index + 1]
#         if sign == '/':
#             if second_num == 0:
#                 print('Делить на ноль')
#                 exit()
#             num[sign_index] = first_num/second_num
#         elif sign == '*':
#             num[sign_index] = first_num*second_num
#         else:
#             num[sign_index] = first_num+second_num
#         del num[sign_index+1]
#         del op[sign_index]

#     for i in '/*+':
#         make_operation(i)


# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности, список повторяемых  и убрать дубликаты из заданной последовательности.


# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и  [1, 3, 5] и [1, 2, 5, 3, 10]

# lst = [1, 2, 3, 5, 1, 5, 3, 10]
# lst2, lst3 = [], []

# for i in set(lst):
#     if lst.count(i) > 1:
#         lst3.append(i)
#     else:
#         lst2.append(i)

# print(f'Сгенерированный список: {lst}\n'
#       f'Уникальные элементы: {lst2}\n'
#       f'Дубликаты: {lst3}\n'
#       f'Список без дубликатов: {list(set(lst))}')


# 2

import time 

start = time.time()

print('Дана последовательность чисел: ', sequence := [1, 2, 3, 5, 1, 5, 3, 10] )
print('Уникальные элементы: ', [n for n in set(sequence) if sequence.count(n) == 1])
print('Дубликаты: ', [n for n in set(sequence) if sequence.count(n) > 1])
print("Список без дубликатов: ", list(set(sequence)))

end = time.time() - start

print(end)
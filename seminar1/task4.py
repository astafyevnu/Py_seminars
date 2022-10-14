# 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

#     *Примеры:*

#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

# 1
# num = abs(float(input("input number: ")))
# print(int(num*10) % 10 if int(num * 10) % 10 != 0 else "no")

# 2
# num = float(input("input number: "))
# print(int(abs(num)*10 % 10))

# 3
# string_num = str(float(input("input number: ")))
# print(string_num[string_num.find(".")+1])

# 4
string_num = str(input("input number: "))
print(string_num.split(".")[1][0])

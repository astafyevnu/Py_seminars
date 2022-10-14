# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

#     Примеры:

#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

# print("input numbers")
# nums = []
# for i in range(5):
#     nums.append(int) = int(input("input number"))
# print (f"Max from {nums}: {max(nums)}") 

nums = input("введите 5 чисел через пробел: ").split()
max = int(nums[0])
for i in nums:
    if int(i) > max:
        max = int(i)
print(max)
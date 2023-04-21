# Task 1
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго
# множества. Затем пользователь вводит сами элементы множеств.

# import random
# RANGE_MIN = 0
# RANGE_MAX = 10

# size_a = int(input('Enter size of first list '))
# size_b = int(input('Enter size of second list '))
# list_nums_a = [random.randint(RANGE_MIN, RANGE_MAX) for _ in range(size_a)]
# list_nums_b = [random.randint(RANGE_MIN, RANGE_MAX) for _ in range(size_b)]
# result = []

# print(list_nums_a)
# print(list_nums_b)

# list_nums_a = set(list_nums_a)
# list_nums_b = set(list_nums_b)

# for a in list_nums_a:
#     for b in list_nums_b:
#         if a == b:
#             result.append(a)
#             break

# result.sort()
# print (result)

# Task 2
# Задача 24

import random
RANGE_MIN = 0
RANGE_MAX = 10

size = int(input('Enter amount of bushes '))
list_nums = [random.randint(RANGE_MIN, RANGE_MAX) for _ in range(size)]

list_count = []

print(list_nums)

for i in range(len(list_nums) - 1):
    list_count.append(list_nums[i - 1] + list_nums[i] + list_nums[i + 1])

print(max(list_count))
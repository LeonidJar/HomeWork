# Task 1
# Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# num_1 = int(input('Enter first number '))
# diff = int(input('Enter difference '))
# amount = int(input('Enter amount of numbers '))
# list_1 = []

# for i in range(amount):
#     list_1.append(num_1 + diff * i)

# print(list_1)


# Task 2
# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

print(list_1 := [random.randint(1, 100) for _ in range(20)])
num_1 = int(input('Enter min '))
num_2 = int(input('Enter max '))

for i in range(len(list_1)):
    if num_1 < list_1[i] < num_2:
        print(i, end = ' ')

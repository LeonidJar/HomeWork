# Task 1
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

# import random

# n = int(input('Enter amount of coins '))
# current = 0
# amount_1 = 0
# amount_0 = 0

# while n > 0:
#     current = random.randint(0, 1)
#     print(current, end = ' ')
#     n -= 1
#     if current == 0:
#         amount_0 += 1
#     else:
#         amount_1 += 1

# if amount_0 > amount_1:
#     print(f'\nMin amount of coins to flip is {amount_1}')
# elif amount_0 < amount_1:
#     print(f'\nMin amount of coins to flip is {amount_0}')
# else:
#     print('doesnt matter')


# Task 2
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# import math

# sum = int(input('Enter sum of 2 numbers '))
# multy = int(input('Enter multiplication of 2 numbers '))

# d = sum * sum - 4 * multy
# x_1 = (sum + math.sqrt(d)) / 2
# x_2 = (sum - math.sqrt(d)) / 2

# if x_1 == x_2 or x_1 == sum - x_2:
#     y = sum - x_1
#     print(f'{int(x_1)} and {int(y)} are original numbers')
# else:
#     if x_1 >= 0:
#         y = sum - x_1
#         print(f'{int(x_1)} and {int(y)} are original numbers')
#     if x_2 >= 0:
#         y = sum - x_2
#         print(f'{int(x_2)} and {int(y)} are original numbers')


# Task 3
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# import random

# n = int(input('Enter a number '))
# current = 2
# i = 1

# while current < n:
#      print(current, end = ' ')
#      i += i
#      current = 2 * i
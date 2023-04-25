# Task 1
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B
# с помощью рекурсии. 

# def power_number(a, b):
#     if b == 1:
#         return a
#     else:
#         return a * power_number(a, b - 1)

# num = int(input('Enter your number '))
# pow = int(input('Enter power '))

# print(power_number(num, pow))


# Task 2
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def summ(a, b):
    if b == 1:
        return a + 1 
    else:
        return summ(a, b - 1) + 1
    
num_1 = int(input('Enter first number '))
num_2 = int(input('Enter second number '))

print(summ(num_1, num_2))
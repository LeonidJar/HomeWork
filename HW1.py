# Task 1
# Найдите сумму цифр трехзначного числа. 

# n = int(input('Enter a three-digit number '))
# m = n

# result = n % 10
# n //= 10

# result += n % 10
# n //= 10

# result += n % 10

# print(m, '->', result)


# Task 2
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# s = int(input('Enter amount of paper cranes '))

# if s % 6 == 0:
#     print(f'{int(s)} -> {int(s / 6)}, {int(s - s / 3)}, {int(s / 6)}')
# else:
#     print('They couldn't do that amount of paper cranes')


# Task 3
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# n = input('Enter a six-digit number of a ticket ')
# i = int(n[0]) + int(n[1]) + int(n[2])
# j = int(n[3]) + int(n[4]) + int(n[5])

# if i == j:
#     print('Yes')
# else:
#     print('No')


# Task 4
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника). 

# print('Enter size of chocolate')
# n = int(input('n = '))
# m = int(input('m = '))

# k = int(input('Enter amount of pieces u need '))

# if k % n == 0 or k % m == 0:
#     print('Yes')
# else:
#     print('No')
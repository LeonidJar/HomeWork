# Task 1
# Задача 16 + 18

# import random
# RANGE_MIN = 0
# RANGE_MAX = 10

# size = int(input('Enter size of list '))
# list_nums = [random.randint(RANGE_MIN, RANGE_MAX) for _ in range(size)]
# count = 0
# min_diff = RANGE_MAX - RANGE_MIN
# closest_num = 0

# print(list_nums)

# k = int(input('Enter your number '))

# for i in list_nums:
#     diff = abs(i - k)
#     if diff < min_diff:
#         closest_num = i
#         min_diff = diff
#     if i == k:
#         count += 1

# if count == 0:
#     print(closest_num)
# else:
#     print(count)


# Task 2
# Scrabble

# list_1 = {'A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'}
# list_2 = {'D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'}
# list_3 = {'B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'}
# list_4 = {'F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'}
# list_5 = {'K', 'Ж', 'З', 'Х', 'Ц', 'Ч'}
# list_8 = {'J', 'X', 'Ш', 'Э', 'Ю'}
# list_10 = {'Q', 'Z', 'Ф', 'Щ', 'Ъ'}

# scrabble = {'1' : list_1, 
#             '2' : list_2,
#             '3' : list_3,
#             '4' : list_4,
#             '5' : list_5,
#             '8' : list_8,
#             '10' : list_10}

# score = 0

# player_word = [x.upper() for x in list(input('Enter your word '))]

# for i in player_word:
#     for item in scrabble:
#         for j in scrabble[item]:
#             if i == j:
#                 score += int(item)

# print(score)

# 1. Необходимо вывести на экран числа от 5 до 1

# counter = 5
# while counter >=1:
#     print(counter)
#     counter -= 1
#
# list_number = range(5, 0, -1) #5- началоб, 0 - конец, -1 - шаг
# print(list(list_number))

# 2. Программа находит сумму чисел от N до M, включая N и M, где N и M вводятся через input()

# number_N = int(input("Введите целое число N: "))
# number_M = int(input("Введите целое число M: "))
# sum_numbers = 0
#
# if number_N < number_M:
#     while number_N <= number_M:
#         sum_numbers += number_N
#         number_N += 1
#     print("Сумма чисел от N до M включительно: ", sum_numbers)
# else:
#     while number_M <= number_N:
#         sum_numbers += number_M
#         number_M += 1
#     print("Сумма чисел от N до M включительно: ", sum_numbers)


# 3. Найти сумму нечётных чисел от N до M, включая N и M, где N и M вводятся через input()

# number_N = int(input("Введите целое число N: "))
# number_M = int(input("Введите целое число M: "))
# sum_numbers = 0
#
# if number_N < number_M:
#     while number_N <= number_M:
#         if (number_N % 2) != 0:
#             sum_numbers += number_N
#         number_N += 1
#     print("Сумма нечетных чисел от N до M включительно: ", sum_numbers)
# else:
#     while number_M <= number_N:
#         if (number_M % 2) != 0:
#             sum_numbers += number_M
#         number_M += 1
#     print("Сумма нечетных чисел от N до M включительно: ", sum_numbers)

# 4. Найти количество нечётных чисел в списке

# list_numbers = range(0, 20, 1)
# print(list(list_numbers))
# sum_numbers = 0
#
# for number in list_numbers:
#     if (number % 2) != 0:
#         sum_numbers += number
#
# print("Сумма нечетных чисел в списке: ", sum_numbers)

# 5. Вывести первые 12 степеней числа 2

# count = 1
# number = 2
# degree = 12
# while count <= degree:
#     print(f"{number} в cтепени {count}: {pow(number,count)}")
#     count +=1
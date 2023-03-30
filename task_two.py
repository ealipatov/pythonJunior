# 2. ДЗ. Найти сумму чётных чисел от N до M, включая N и M, где N и M вводятся через input().
# Учесть условие когда первое число больше второго


number_N = int(input("Введите целое число N: "))
number_M = int(input("Введите целое число M: "))


def sum_numbers(n, m):
    _sum = 0
    while n <= m:
        if (n % 2) == 0:
            _sum += n
        n += 1
    return _sum


if number_N < number_M:
    print(f"Сумма четных чисел от {number_N} до {number_M} включительно: {sum_numbers(number_N, number_M)}")
else:
    print(f"Сумма четных чисел от {number_M} до {number_N} включительно: {sum_numbers(number_M, number_N)}")

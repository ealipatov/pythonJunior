# 1. ДЗ. Вывести на экран произведение чисел от -10 до 7

# так как в условии задания ничего не говорится про умножение на 0 (а 0 это тоже число),
# то результат для диапазона чисел, где одно отрицательное а второе положительное, всегда будет равен нулю

number_N = -10
number_M = 7


def number_operation_with_zero(n, m):
    result = 1
    while n <= m:
        result *= n
        n += 1
    return result


def number_operation_without_zero(n, m):
    result = 1
    while n <= m:
        if n == 0:
            n += 1
        else:
            result *= n
            n += 1
    return result


def print_result_with_zero():
    if number_N < number_M:
        print(f"Произведение чисел от {number_N} до {number_M} включительно (включая ноль): "
              f"{number_operation_with_zero(number_N, number_M)}")
    else:
        print(f"Произведение чисел от {number_M} до {number_N} включительно: "
              f"{number_operation_with_zero(number_M, number_N)}")

def print_result_without_zero():
    if number_N < number_M:
        print(f"Произведение чисел от {number_N} до {number_M} включительно: "
              f"{number_operation_without_zero(number_N, number_M)}")
    else:
        print(f"Произведение чисел от {number_M} до {number_N} включительно: "
              f"{number_operation_without_zero(number_M, number_N)}")


temp = int(input("Учитывать число ноль в диапазоне чистел? (0 - да, 1 - нет): "))

if temp == 0:
    print_result_with_zero()
elif temp == 1:
    print_result_without_zero()
else:
    print(f"Введен некорректный символ.")

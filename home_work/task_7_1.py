# Найти сумму цифр числа, кроме самой левой цифры(Самый старший разряд)

def sum_number(num):
    _sum = 0
    pos_num = abs(num)
    while len(str(pos_num)) > 1:
        digit = pos_num % 10
        _sum += digit
        pos_num //= 10
    return _sum


number = 23456

print(f"Сумма цифр числа {number}: {sum_number(number)}\n")

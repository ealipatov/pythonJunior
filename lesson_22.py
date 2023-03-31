# 1. Найти сумму цифр числа
print("1. Найти сумму цифр числа\n")


def sum_number(number):
    _sum = 0
    number = abs(number)
    while number > 0:
        digit = number % 10
        _sum += digit
        number //= 10
    return _sum


number = 12345

print(f"Сумма цифр числа {number}: {sum_number(number)}\n")


# 2. Найти максимальное чётное число из случайного набора чисел(Сгенерировать случайный набор чисел)

print("2. Найти максимальное чётное число из случайного набора чисел(Сгенерировать случайный набор чисел)\n")
from random import randint

numbers = []
count = 0
while count < 20:
    numbers.append(randint(1, 1000))
    count += 1
print(numbers)

max_even_num = 0
for num in numbers:
    if (num > max_even_num) and (num % 2 == 0):
        max_even_num = num
print(f"Максимальное четное число в списке: {max_even_num}\n")

# 3. Отсортировать список от меньшего к большему не используя функцию sort()

print("3. Отсортировать список от меньшего к большему не используя функцию sort()\n")

numbers = []
numbers_sorted = []
counter = 0
while counter < 10:
    numbers.append(randint(1, 1000))
    counter += 1
print(numbers)
while len(numbers) != 0:
    min_number = 10000
    for number in numbers:
        if number < min_number:
            min_number = number
    numbers.remove(min_number)
    numbers_sorted.append(min_number)
print(numbers_sorted)

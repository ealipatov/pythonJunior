# Найти минимальное нечётное число из случайного набора чисел(Сгенерировать случайный набор чисел)

from random import randint

numbers = []
count = 0
while count < 20:
    numbers.append(randint(1, 1000))
    count += 1
print(numbers)

min_odd_num = max(numbers)
for num in numbers:
    if (num < min_odd_num) and (num % 2 != 0):
        min_odd_num = num
print(f"Минимальное нечетное число в списке: {min_odd_num}\n")

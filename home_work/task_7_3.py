# ДЗ. Отсортировать список от большего к меньшему не используя функцию sort()

from random import randint

numbers = []
numbers_sorted = []
counter = 0
while counter < 10:
    numbers.append(randint(1, 1000))
    counter += 1
print(numbers)

# Сортировка пузырьком
for i in range(len(numbers) - 1):
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print(numbers)

while len(numbers) != 0:
    max_number = 0
    for number in numbers:
        if number > max_number:
            max_number = number
    numbers.remove(max_number)
    numbers_sorted.append(max_number)
print(numbers_sorted)

#3.ДЗ. Найти количество кратных 10 (10, 20, 30 ...) чисел в списке


list_numbers = range(10, 100, 10)
print(list(list_numbers))
counter = 0

for number in list_numbers:
    if (number % 10) == 0:
        counter += 1

print(f"Количество чисел в списке кратных 10: {counter}")

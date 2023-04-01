string_one = "Привет"
string_two = "всем"
number = [1, 2, 3, 4, 5]
letter = ["1", "2", "3", "4", "5"]

print(string_one + " " + string_two)
print("Привет %s" % string_two)
print("Привет %s %s %s" % (string_two, string_two, string_two))
print(f"{string_one} {string_two}")

text = "Мой дядя самых честных правил"
print(text)
print(text[:10])  # Выведет на экран первые 10 символов строки
print(text[10:])  # Выведет на экран все символы строки после 10-го символа
print(text[10:20])  # Выведет на экран символы строки c 10-го по 20-ый символ
print(text[-10:])  # Выведет на экран 10 символов с конца строки

# for symbol in text:
#     print(symbol)

print(text.upper())  # Выведет всю строку заглавными
print(text.split(" "))  #  разобьет строку на список с разделением по "_" пробелу
print(text.replace("м", "М"))  # Замена символов или слов в строке

print(" ".join(letter))  # Преобразование списка строковых элементов в строку

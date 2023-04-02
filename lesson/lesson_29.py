year_list = [1981, 1982, 1983, 1984, 1985, 1986]
print(f"Мой третий день рождения был в {year_list[2]}")
print(f"Больше всего лет из списка мне было в {year_list[len(year_list) - 1]}")  # или year_list[-1] - последний элемент

print("-" * 80)

things = ["mozzarella", "cinderella", "salmonella"]
print(things[1].title())  # вывести элемент списка с большой буквы
# print(things[1].replace("c", "C"))  # заменить букву в списке!!!
print(things[1][0].upper() + things[1][1:])  # выведем заглавной только первую буквы, потом остальное
print(things[0].upper())

# things.pop(2)  # удаление по индексу
things.remove("salmonella")  # удаление по значению
print(things)

print("-" * 80)

surprise = ["Groucho", "Chico", "Harpo"]
print(surprise)
# print(surprise[2][0].lower() + surprise[2][1:])
surprise.remove("Harpo")
surprise.append("harpo")
print(surprise)

print("-" * 80)

e2f = {
    "dog": "chien",
    "cat": "chat",
    "walrus": "morse"
}

f2e = {}

for eng, france in e2f.items():
    f2e[france] = eng  # в словарь добавляем элементы с ключом [franse] и значением eng

print(e2f["walrus"])  # вывести значение из словаря по ключу walrus
print(f2e["chien"])
print(list(e2f.keys()))
print(e2f)
print(f2e)

print("-" * 80)

life = {
    "animals": {
        "cats": ["Henri", "Grumpy", "Lucy"],
        "octopi": [],
        "enum": []
    },
    "plants": {},
    "other": {}
}

print(life)
print(list(life.keys()))
print(list(life["animals"].keys()))
print(list(life["animals"]["cats"]))
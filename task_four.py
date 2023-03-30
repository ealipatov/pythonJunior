#4.ДЗ. Вывести первые 7 степеней числа 3

count = 1
number = 3
degree = 7
while count <= degree:
    print(f"{number} в cтепени {count}: {pow(number,count)}")
    count +=1
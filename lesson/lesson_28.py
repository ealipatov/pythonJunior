hour = int(input("Введите количнство часов: "))
print(f"В {hour} часах {hour * 60 * 60} секунд")

seconds_per_hour = 1 * 60 * 60
seconds_per_day = seconds_per_hour * 24

print(f"В часе {seconds_per_hour} секунд, в одних сутках {seconds_per_day} секунд")

print(seconds_per_day / seconds_per_hour)  # Деление с точностью до запятой
print(seconds_per_day // seconds_per_hour)  # Деление с точностью только целой части (без запятой)

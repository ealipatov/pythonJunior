# Игра против компьютера
from random import randint

start_number = 1
end_number = 1000
number = randint(start_number, end_number)
player_name = input("Введите имя игрока: ")
computer_name = "Мегамозг"
check_end_game = True

print(f"Игра угадай число от {start_number} до {end_number}")


def check_number(num, player):
    if num == number:
        print(f"{player} победил! Игра окончена")
        return True
    elif num > number:
        print(f"Загаданное число меньше {num}")
        return False
    else:
        print(f"Загаданное число больше {num}")
        return False


while check_end_game:
    player_number = int(input(f"{player_name} введите число: "))
    if check_number(player_number, player_name):
        break

    print("\nХод компьютера")
    computer_number = randint(start_number, end_number)
    if check_number(computer_number, computer_name):
        break

def display_menu():
    print("Выбери действие: 1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление, 0 - выход")
    choice = input("Введи номер действия: ")
    return choice

def get_numbers():
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    return num1, num2

def show_result(result):
    print("Результат:", result)

def show_message(message):
    print(message)

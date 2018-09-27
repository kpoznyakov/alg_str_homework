# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

# Начало
# Ввод ("Введите число" n)
# Алфавит = ("abcdefghijklmnopqrstuvwxyz")
# Если n больше нуля и меньше или равно длине алфавита, то
#     Вывод ("Буква '{alphabet[n - 1]}' имеет номер '{n}'.")
# Иначе
#     Вывод ("Нет буквы с таким номером")


def symb_from_num(n):
    alphabet = ("abcdefghijklmnopqrstuvwxyz")
    if n <= len(alphabet) and n > 0:
        print(f"Буква '{alphabet[n - 1].upper()}' имеет номер '{n}'.")  # Upper для красоты
    else:
        print("Нет буквы с таким номером")


try:
    n = int(input("Введите номер буквы в алфавите - "))
    symb_from_num(n)
except ValueError:
    print("Введите число")

# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в ее последнюю ячейку.
# В конце следует вывести полученную матрицу.

from pprint import pprint

while True:
    try:
        matrix = [[int(input("Введите данные для заполнения матрицы: ")) for _ in range(4)] for _ in range(4)]
        break
    except ValueError:
        print("Вводите цифры. Попробуйте еще раз.")
        continue

c = 0
for c in range(0, len(matrix)):
    matrix[c].append(f"SUM = {sum(matrix[c])}")
    c += 1

pprint(matrix)

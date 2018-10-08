# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.


import random

matrix = [[random.randint(1, 100) for _ in range(3)] for _ in range(3)]

print(matrix)

min_column = [float('inf')] * len(matrix[0])
max_of_min = -float('inf')

for line in matrix:
    for idx, val in enumerate(line):
        if val < min_column[idx]:
            min_column[idx] = val

print(min_column)

for i in min_column:
    if i > max_of_min:
        max_of_min = i
print("max_of_min =", max_of_min)

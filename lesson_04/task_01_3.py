# 1. Проанализировать скорость и сложность одного - трёх любых алгоритмов,
# разработанных в рамках домашнего задания первых трех уроков.
# Примечание: Результаты анализа сохранить в виде комментариев в файле с кодом.

# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.


import random
import cProfile


def maxmin(st, col):
    matrix = [[random.randint(-10, 100) for _ in range(st)] for _ in range(col)]

    # print(matrix)

    min_column = [float('inf')] * len(matrix[0])
    max_of_min = float('-inf')

    for line in matrix:
        for idx, val in enumerate(line):
            if val < min_column[idx]:
                min_column[idx] = val

    # print(min_column)

    for i in min_column:
        if i > max_of_min:
            max_of_min = i
    # print("max_of_min =", max_of_min)


# maxmin(5, 5)

# 100 loops, best of 3: 46.1 usec per loop  - task_01_3.maxmin(5, 5)
# 100 loops, best of 3: 165 usec per loop   - task_01_3.maxmin(10, 10)
# 100 loops, best of 3: 4.07 msec per loop  - task_01_3.maxmin(50, 50)
# 100 loops, best of 3: 15.5 msec per loop  - task_01_3.maxmin(100, 100)
# 100 loops, best of 3: 390 msec per loop   - task_01_3.maxmin(500, 500)


cProfile.run('maxmin(1000, 1000)')
# 1    0.000    0.000    0.000    0.000 task_01_3.py:12(maxmin) - cProfile.run('maxmin(10, 10)')
# 1    0.001    0.001    0.024    0.024 task_01_3.py:12(maxmin) - cProfile.run('maxmin(100, 100)')
# 1    0.020    0.020    0.610    0.610 task_01_3.py:12(maxmin) - cProfile.run('maxmin(500, 500)')
# 1    0.082    0.082    2.373    2.373 task_01_3.py:12(maxmin) - cProfile.run('maxmin(1000, 1000)')


# O(n) – линейная сложность, наверное. Так как пробегаемся 1 раз по столбцам а второй раз по результатам.
# А можно описать как O(n)2?

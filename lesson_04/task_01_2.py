# 1. Проанализировать скорость и сложность одного - трёх любых алгоритмов,
# разработанных в рамках домашнего задания первых трех уроков.
# Примечание: Результаты анализа сохранить в виде комментариев в файле с кодом.

# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 0, 3, 4, 5 (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.


import random
import cProfile


def array(r):
    array = [random.randint(0, 100) for i in range(r)]
    # print("Исходный массив:", array)
    res = []
    for i, idx in enumerate(array):
        if idx % 2 == 0:
            res.append(i)
    # print("Индексы кратные двум:", res)


# 100 loops, best of 3: 17.1 usec per loop  - task_01_2.array(10)
# 100 loops, best of 3: 1.62 msec per loop  - task_01_2.array(1000)
# 100 loops, best of 3: 170 msec per loop   - task_01_2.array(100000)


cProfile.run('array(10000000)')
# 1    0.000    0.000    0.000    0.000 task_01_2.py:15(array)  - cProfile.run('array(10)')
# 1    0.000    0.000    0.003    0.003 task_01_2.py:15(array)  - cProfile.run('array(1000)')
# 1    0.018    0.018    0.253    0.253 task_01_2.py:15(array)  - cProfile.run('array(100000)')
# 1    1.701    1.701   24.914   24.914 task_01_2.py:15(array)  - cProfile.run('array(10000000)')

# O(n) — линейная сложность

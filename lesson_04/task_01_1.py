# 1. Проанализировать скорость и сложность одного - трёх любых алгоритмов,
# разработанных в рамках домашнего задания первых трех уроков.
# Примечание: Результаты анализа сохранить в виде комментариев в файле с кодом.

# 4. Найти сумму n элементов следующего ряда чисел:
# 1, -0.5, 0.25, -0.125, ...
# Количество элементов (n) вводится с клавиатуры.

import cProfile


# n = int(input("Сколько элементов будем считать? - "))


def r(n):
    start = 1
    res = 0

    for i in range(n):
        res += start
        start /= -2  # Скажу честно - без подсказки не догадался бы
        # print(start)
    # print("Сумма = ", res)


# 100 loops, best of 3: 0.529 usec per loop     - task_01_1.r(1)
# 100 loops, best of 3: 1.27 usec per loop      - task_01_1.r(10)
# 100 loops, best of 3: 7.5 usec per loop       - task_01_1.r(100)
# 100 loops, best of 3: 80.6 usec per loop      - task_01_1.r(1000)
# 100 loops, best of 3: 842 usec per loop       - task_01_1.r(10000)
# 100 loops, best of 3: 8.45 msec per loop      - task_01_1.r(100000)
# 100 loops, best of 3: 85.6 msec per loop      - task_01_1.r(1000000)
# 100 loops, best of 3: 848 msec per loop       - task_01_1.r(10000000)

cProfile.run('r(10000000)')
# 1    0.000    0.000    0.000    0.000 task_01_1.py:15(r)      - cProfile.run('r(1)')
# 1    0.000    0.000    0.000    0.000 task_01_1.py:15(r)      - cProfile.run('r(100)')
# 1    0.000    0.000    0.000    0.000 task_01_1.py:15(r)      - cProfile.run('r(1000)')
# 1    0.001    0.001    0.001    0.001 task_01_1.py:15(r)      - cProfile.run('r(10000)')
# 1    0.009    0.009    0.009    0.009 task_01_1.py:15(r)      - cProfile.run('r(100000)')
# 1    0.084    0.084    0.084    0.084 task_01_1.py:15(r)      - cProfile.run('r(1000000)')
# 1    0.852    0.852    0.852    0.852 task_01_1.py:15(r)      - cProfile.run('r(10000000)')


# O(n) — линейная сложность
# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Первый - использовать алгоритм решето Эратосфена.
# Второй - без использования "решета".
# Проанализировать скорость и сложность алгоритмов.

import cProfile


# "Решето Эратосфена", сложность O((n)*(log(log(n))))
# def er(n):
#     non_prim = set()
#     i = 1
#
#     while n != 0:
#         i += 1
#
#         if i not in non_prim:
#             for j in range(i * i, n * n, i):
#                 non_prim.add(j)
#             n -= 1
#     return i

# print(er(10))


# 100 loops, best of 3: 12.9 usec per loop  -   task_02.er(10)
# 100 loops, best of 3: 1.86 msec per loop  -   task_02.er(100)
# 100 loops, best of 3: 8.54 msec per loop  -   task_02.er(200)
# 100 loops, best of 3: 21 msec per loop    -   task_02.er(300)
# 100 loops, best of 3: 46.3 msec per loop  -   task_02.er(400)
# 100 loops, best of 3: 78.3 msec per loop  -   task_02.er(500)

# cProfile.run('er(10000)')
# 1    0.000    0.000    0.000    0.000 task_02.py:10(er)   cProfile.run('er(10)')
# 1    0.002    0.002    0.004    0.004 task_02.py:10(er)   cProfile.run('er(100)')
# 1    0.312    0.312    0.640    0.640 task_02.py:10(er)   cProfile.run('er(1000)')
# 1   36.106   36.106   96.728   96.728 task_02.py:10(er)   cProfile.run('er(10000)')


def prime(n):
    i = 2
    c = 0

    while True:
        for d in range(2, i + 1):
            if i % d == 0:
                if i == d:
                    c += 1
                break

        if c == n:
            break

        i += 1
    return i


# print(prime(10))

# 100 loops, best of 3: 21.5 usec per loop  -   task_02.prime(10)
# 100 loops, best of 3: 1.65 msec per loop  -   task_02.prime(100)
# 100 loops, best of 3: 7.85 msec per loop  -   task_02.prime(200)
# 100 loops, best of 3: 19.8 msec per loop  -   task_02.prime(300)
# 100 loops, best of 3: 37.3 msec per loop  -   task_02.prime(400)
# 100 loops, best of 3: 61.8 msec per loop  -   task_02.prime(500)

cProfile.run('prime(10000)')
# 1    0.000    0.000    0.000    0.000 task_02.py:40(prime)    cProfile.run('prime(10)')
# 1    0.002    0.002    0.002    0.002 task_02.py:40(prime)    cProfile.run('prime(100)')
# 1    0.281    0.281    0.281    0.281 task_02.py:40(prime)    cProfile.run('prime(1000)')
# 1   38.684   38.684   38.684   38.684 task_02.py:40(prime)    cProfile.run('prime(10000)')


# Вывод - на современных быстрых компьютерах можно не заморачиваться с решетом Эратосфена для
# вычислений простого числа до 10000, так как разницы по времени практически не будет
# и вообще я ожидлал что второй подход будет медленнее

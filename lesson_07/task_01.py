# 1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Вывести на экран исходный и отсортированный массивы.
import random
import cProfile


def bubble_sort(arr):
    n = 1
    while n < len(arr):
        for i in range(len(arr) - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        n += 1
    return arr


def bubble_sort_on_steroids(arr):  # в разы быстрее!
    for i in range(arr.index(arr[-1]), 0, -1):  # просто проверил замену len(arr) - 1 #
        rev = False
        for j in range(i, 0, -1):
            if arr[j] > arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                rev = True
        for j in range(i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                rev = True

        if not rev:
            return arr


array = [random.randrange(-100, 100) for i in range(1000)]
# randint (любое число из) бы сделал включительно, а randrange (любой число в промежутке от - до) делает исключительно


print(array)

print(bubble_sort(array))
print(bubble_sort_on_steroids(array))

cProfile.run('bubble_sort(array * 10)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000   10.286   10.286 <string>:1(<module>)
#      1   10.283   10.283   10.286   10.286 task_01.py:7(bubble_sort)
#      1    0.000    0.000   10.286   10.286 {built-in method builtins.exec}
#  19999    0.003    0.000    0.003    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('bubble_sort_on_steroids(array * 10)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 task_01.py:17(bubble_sort_on_steroids)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

cProfile.run('bubble_sort_on_steroids(array * 10000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.071    0.071    0.071    0.071 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 task_01.py:17(bubble_sort_on_steroids)
#      1    0.000    0.000    0.071    0.071 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

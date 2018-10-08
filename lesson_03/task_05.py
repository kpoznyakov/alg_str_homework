# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

array = [random.randint(-100, 100) for i in range(10)]
print(array)

max_minimum = -float('inf')
pos = None
for key, val in enumerate(array):
    if 0 > val > max_minimum:
        max_minimum = val
        pos = key
print(f"Минимальное отрицательное число {max_minimum} находится по индексу {pos}.")

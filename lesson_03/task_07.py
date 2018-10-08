# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

array = [random.randint(-100, 100) for i in range(10)]
# array = [-1, 2, 3, 4, 5, -60, 7, 8, 9, -10]


print("Исходник:\t", array)

minimum = float('inf')
next_minimum = minimum
key_of_minimum = 0
for k, v in enumerate(array):
    if v < minimum:
        minimum = v
        key_of_minimum = k

for k2, v2 in enumerate(array):
    if k2 == key_of_minimum:
        continue
    else:
        if v2 < next_minimum:
            next_minimum = v2
print("Минимум =", minimum, "| Следующее после минимума =", next_minimum)

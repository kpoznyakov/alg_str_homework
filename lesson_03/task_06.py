# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

array = [random.randint(-100, 100) for i in range(10)]

print("Исходник:\t", array)

minimum = float('inf')  # не придумал ничего лучше чем это для определения int переменной
maximum = -float('inf')

for k, v in enumerate(array):
    if v > maximum:
        maximum = v
        max_key = k

    if v < minimum:
        minimum = v
        min_key = k

res = 0
for i in array[
         min_key + 1:max_key]:  # не понял как нужно обработать ситуацию если максимальный стоит перед минимальным.
    # Ниже закоменченное решение если надо было посчитать
    res += i
print(f"Сумма элементов между мин. и макс. значениями в массиве ({array[min_key+1:max_key]}) =", res)

# res2 = 0
# if min_key > max_key:
#     # print("min_key, max_key", min_key, max_key)
#     for i2 in array[max_key+1:min_key]:
#         res2 += i2
# print(f"Сумма элементов между мин. и макс. значениями в массиве ({array[max_key+1:min_key]}) =", res2)

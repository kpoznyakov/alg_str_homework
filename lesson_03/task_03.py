# # 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
#
#
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

array[min_key], array[max_key] = array[max_key], array[min_key]

print("Результат:\t", array)

# кривое решение - переделал
# def find_min(arr):
#     minimum = float('inf')
#     for i in range(len(arr)):
#         if arr[i] < minimum:
#             minimum = arr[i]
#             minimum_index = i
#     return minimum, minimum_index  # можно узнать значение вызвав find_min(array)[0]
#
#
# def find_max(arr):
#     maximum = -float('inf')
#     for i in range(len(arr)):
#         if arr[i] > maximum:
#             maximum = arr[i]
#             maximum_index = i
#     return maximum, maximum_index

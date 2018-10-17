# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найти в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше ее.
#
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# то используйте метод сортировки, который не рассматривался на уроках.

import random
import statistics

array = [random.randrange(-100, 100) for i in range((2 * random.randint(0, 10)) + 1)]
print("Исходный массив -", array)


# print("Cheat median =", statistics.median(array))

def bogosort(collection):  # нашел одну из самх идиотских сортировок :) Не запускать на больших числах!
    def isSorted(collection):
        if len(collection) < 2:
            return True
        for i in range(len(collection) - 1):
            if collection[i] > collection[i + 1]:
                return False
        return True

    while not isSorted(collection):
        random.shuffle(collection)
    return collection


sort = bogosort(array)
print(sort[len(sort) // 2])

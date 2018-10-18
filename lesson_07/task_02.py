# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.


import random


def split_(input_list):  # разбиваем массив пополам
    mid = len(input_list) // 2  # ищем почти средний элемент в массиве
    return input_list[:mid], input_list[mid:]  # возвращаем 2 массива с индексами от 0 до mid и от mid до конца


def merge_sorted_lists(left_side, right_side):
    if len(left_side) == 0:  # проверка на то что в массиве что-то осталось вообще
        return right_side
    elif len(right_side) == 0:  # обязательно проверяем обе половинки
        return left_side

    index_left = index_right = 0  # присваиваем двум переменным одинаковое значение
    list_merged = []  # создаем пустой список который будем заполнять и возвращать
    list_len_target = len(left_side) + len(right_side)  # узнаем сколько индексов должно быть в массиве всего
    while len(list_merged) < list_len_target:
        if left_side[index_left] <= right_side[index_right]:  # добавляем значение если оно меньшеравно
            list_merged.append(left_side[index_left])
            index_left += 1  # увеличиваем точку отсчета слева на 1
        else:
            list_merged.append(right_side[index_right])  # добавляем значение если оно большеравно
            index_right += 1  # справа на 1

        # If we are at the end of one of the lists we can take a shortcut
        if index_right == len(right_side):  # если индекс равен длине стороны

            list_merged += left_side[index_left:]  # добавляем часть левого индекса
            break
        elif index_left == len(left_side):  # обязательно проверяем обе части
            list_merged += right_side[index_right:]
            break

    return list_merged


def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    else:
        left, right = split_(input_list)  # получаем 2 половинки массива в цикле пока не останется 1 символ в массиве
        return merge_sorted_lists(merge_sort(left), merge_sort(right))


array = [random.randrange(0, 50) for i in range(11)]
print(array)
print("Sorted -", merge_sort(array))

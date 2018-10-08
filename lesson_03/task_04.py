# 4. Определить, какое число в массиве встречается чаще всего.

import random

array = [random.randint(-100, 100) for i in range(1000)]
# array = [5, 2, 3, 4, 5, 5, 7, 8, 9, 5]
print(array)

max_e = 0
val = array[0]

for i in range(len(array)):
    e = 0
    for j in range(i, len(array)):
        if array[i] == array[j]:
            e += 1

    if e > max_e:
        max_e = e
        val = array[i]

print(f'Число {val} встречается {max_e} раз' if max_e > 1 else 'нет повторов')

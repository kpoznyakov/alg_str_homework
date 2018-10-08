# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.


crat = [0] * 8

for i in range(2, 100):
    for x in range(2, 10):
        if i % x == 0:
            crat[x - 2] += 1
print(crat)

counter = 0
while counter < len(crat):
    print(f"Кратных: {counter + 2} - {crat[counter]}")  # начинаем отсчет счетчика с 2
    counter += 1

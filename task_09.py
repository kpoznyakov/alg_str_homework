# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

average = []

average.append(float(input("Введите первое число - ")))
average.append(float(input("Введите второе число - ")))
average.append(float(input("Введите третье число - ")))

print(f"Среднее из введенных - {sorted(average)[1]:.3f}")

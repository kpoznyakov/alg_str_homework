# 3. По введенным пользователем координатам двух точек вывести уравнение прямой, проходящей через эти точки.

# Начало
# Вывод("Введите координаты двух точек в формате: x1, y1, x2, y2.")
# Ввод(x1, y1, x2, y2)
# Вывод("Точка A(x1, x2), Точка B(y1, y2). Уравнение = y = kx + b")
# Вычисления:
# Если (x1 - x2 != 0) то
#   k = (y1 - y2) / (x1 - x2)
#   b = y2 - k*x2
# Иначе
#   k = 0
# Вывод("y = kx + b")
# Конец

print("Введите координаты точки A в формате: x1, y1")
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))

print("Введите координаты точки B в формате: x2, y2")
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

if (x1 - x2) != 0:  # Возможно тут надо еще делать проверки на то что b может равняться нулю..
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
else:
    k = 0
    b = y2 - k * x2

print(f"Уравнение прямой будет таким: y = {k} * x + {b}")
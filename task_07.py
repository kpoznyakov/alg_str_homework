# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков.
# Если такой треугольник существует, то определить, является ли он
# разносторонним, равнобедренным или равносторонним.


segm = []

segm.append(int(input("Введите длину отрезка '1' (целое число) - ")))
segm.append(int(input("Введите длину отрезка '2' (целое число) - ")))
segm.append(int(input("Введите длину отрезка '3' (целое число) - ")))

segm = sorted(segm)

if segm[0] + segm[1] <= segm[2]:
    print("Треугольник не может существовать :(")
    exit()
elif segm[0] == segm[1] == segm[2]:
    print("Равносторонний треугольник может существовать!")
elif segm[0] == segm[1] or segm[1] == segm[2] or segm[0] == segm[2]:
    print("Равнобедренный треугольник может существовать!")
else:
    print("Разносторонний треугольник может существовать!")

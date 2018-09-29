# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

z = input("Введите целое число - ")
n = int(z)
res = 0
begin_z_counter = str()
end_z_counter = str()

if z.count('0') == len(z):
    print(f'Перевернутое - {z}')
else:
    while n > 0:
        x = n % 10
        n = n // 10
        res = res * 10
        res = res + x

    c = 0
    for i in z:
        if int(z[c]) == 0:
            begin_z_counter = begin_z_counter + "0"
            c += 1

    c = -1
    for i in z:
        if int(z[c]) == 0:
            end_z_counter = end_z_counter + "0"
            c += -1

    print(f'Перевернутое - {end_z_counter}{res}{begin_z_counter}')

# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
# Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

import collections

d = {'0': 0,
     '1': 1,
     '2': 2,
     '3': 3,
     '4': 4,
     '5': 5,
     '6': 6,
     '7': 7,
     '8': 8,
     '9': 9,
     'A': 10,
     'B': 11,
     'C': 12,
     'D': 13,
     'E': 14,
     'F': 15,
     }


def hex_to_dec(hex_num):
    dq = list(reversed(collections.deque(hex_num)))
    res = 0
    for i, v in enumerate(dq):
        try:
            res += d[v] * (16 ** i)
        except KeyError:
            exit('"-" найден в числе. Его там быть не должно!')
    return res


def dec_to_hex(dec_num):
    inv_map = {v: k for k, v in d.items()}
    DEC = 16
    hex_list = []
    while dec_num > 0:
        hex_list += [inv_map[dec_num % DEC]]
        dec_num //= DEC
    return list(reversed(hex_list))


def check_negative(n):
    if n.startswith('-'):
        print('- FOUND!')


negative_1 = False
negative_2 = False

print("Введи 2 шестнадцатиричных числа:")
num1 = (input("Первое число = "))
if num1.startswith('-'):
    negative_1 = True
    num1 = num1[1:]
num2 = (input("Второе число = "))
if num2.startswith('-'):
    negative_2 = True
    num2 = num2[1:]

num = [num1.upper(), num2.upper()]

for val in num:
    # print(val)
    for val2 in val:
        if val2 not in d and val2 != '-':
            print(f"Используй {''.join(list(d.keys()))}. Попробуй еще раз.")
            exit('ERR')

summ = 0
mult = 0

if negative_1 is False and negative_2 is False:
    summ = int(hex_to_dec(num[0])) + int(hex_to_dec(num[1]))
    mult = int(hex_to_dec(num[0])) * int(hex_to_dec(num[1]))
    print(f"Сумма = {''.join(dec_to_hex(summ))}")
    print(f"Произведение = {''.join(dec_to_hex(mult))}")
elif negative_1 is True:  # не хватило времени на проверку отрицательного числа :(
    summ = int(hex_to_dec(num[0])) + int(hex_to_dec(num[1]))
    mult = int(hex_to_dec(num[0])) * int(hex_to_dec(num[1]))
    print(f"Сумма = {''.join(dec_to_hex(summ))}")
    print(f"Произведение = {''.join(dec_to_hex(mult))}")

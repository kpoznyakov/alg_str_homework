# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего.
# # Примечание: 4 квартала - это 4 разных прибыли ;-)


import collections


class Company:
    def __init__(self, name):
        self.name = name
        self.quarter_profit = collections.deque([], maxlen=4)

    def add_profit(self, summ):
        self.quarter_profit.append(summ)

    def average_profit(self):
        return sum(self.quarter_profit) / len(self.quarter_profit)

    def full_profit(self):
        return sum(self.quarter_profit)


n_companies = 0
try:
    n_companies = +int(input("Сколько предприятий в вашем бизнес-центре? - "))
except ValueError:
    exit("Вводите числа (целые)!")

if n_companies <=0:
    exit('Нет смысла считать.')

print("*" * 10)
comp_names = []
for n in range(n_companies):
    comp_names.append('Company_ID_' + str(n + 1))

all_profit = 0
average_all_profit = 0

higher = []
lower = []
classes = collections.deque([], maxlen=n_companies)  # кажется на больших n_companies все тормозит.

for i in comp_names:
    i = Company(i)
    for n in range(4):
        try:
            i.add_profit(int(input(f"Сколько компания '{i.name}' заработала в квартале '{n+1}' = ")))
        except ValueError:
            exit("Вводите числа")
    print(f"Средняя квартальная прибыль отдельного предприятия: '{i.name}' = {i.average_profit()}")
    classes.append(i)
    all_profit += i.full_profit()
    print("*" * 10)

try:
    average_all_profit = all_profit / n_companies
except ZeroDivisionError:
    exit("Никто не снимает помещения в вашем жалком бизнес-центре.")

print("Общая прибыль за год всех предприятий =", all_profit)
print("Общая средняя прибыль за год со всех предприятий =", average_all_profit)

for el in classes:
    if el.full_profit() >= average_all_profit:
        higher.append(el.name)
    if el.full_profit() <= average_all_profit:
        lower.append(el.name)

print("Выше среднего заработали следующие предприятия: ", higher)
print("Ниже среднего заработали следующие предприятия: ", lower)

import pandas as pd
import math
import scipy
import numpy as np
import statsmodels.api as sm
import statistics
from statistics import mean
from statistics import pstdev
# import matplotlib.pyplot as plt
# import seaborn as sns

data = pd.read_excel('data/crimePrav.xlsx')


def test_asymmetry(lst):  # Проверка нормальности по асимметрии
    asymmetry_krit = (6 * (len(lst) - 2) / ((len(lst) + 1) * (len(lst) + 3))) ** 0.5 * 3
    if abs(scipy.stats.skew(lst, bias=False)) > asymmetry_krit:
        flag = 0
    else:
        flag = 1
    return flag


def test_eks(lst):  # Проверка нормальности по эксцессу
    eks_krit = ((24 * len(lst) * (len(lst) - 2) * (len(lst) - 3)) / (
                (len(lst) + 5) * (len(lst) + 3) * ((len(lst) + 1) ** 2))) ** 0.5 * 5
    if abs(scipy.stats.kurtosis(lst, bias=False)) > eks_krit:
        flag = 0
    else:
        flag = 1
    return flag


def normalize():  # Удаление аномалий
    index = 0
    while index < len(ResultList):
        j = 0
        mid = mean(ResultList[index])
        standard = 3 * pstdev(ResultList[index])
        while j < len(ResultList[index]):
            if ResultList[index][j] > mid + standard or ResultList[index][j] < mid - standard:
                del ResultList[index][j]
                for ind in range(len(ResultList)):
                    if ind != index:
                        del ResultList[ind][j]
            j += 1
        index += 1


def empty():  # Удаление пустых значений
    index = 0
    while index < len(ResultList):
        j = 0
        while j < len(ResultList[index]):
            if np.isnan(ResultList[index][j]):
                del ResultList[index][j]
                for ind in range(len(ResultList)):
                    if ind != index:
                        del ResultList[ind][j]
                continue
            j += 1
        index += 1


def correlation():  # Расчёт корреляции
    return statistics.correlation(ResultList[0], ResultList[1])


def significance_test(kor, length):  # Проверка значимости корреляции
    alpha = 0.05
    sample_value = (kor * math.sqrt(length - 2)) / math.sqrt(1 - (kor ** 2))
    theoretical_value = scipy.stats.t.isf(alpha / 2, length - 2)
    if abs(sample_value) > theoretical_value:
        return 1
    return 0


def regress():  # Регрессия
    x1 = sm.add_constant(X)
    reg = sm.OLS(Y, x1).fit()
    return reg.summary()


# КОРРЕЛЯЦИЯ____________________________________________________________________________________________________________)

while True:
    print("Выбор первого столбца для корреляции: ")
    index1 = int(input())
    if index1 not in (3, 4, 6, 7, 8, 9):
        print("Такого столбца нет или он имеет не числовое значение!")
        continue
    break

while True:
    print("Выбор второго столбца для корреляции: ")
    index2 = int(input())
    if index2 not in (3, 4, 6, 7, 8, 9) or index2 == index1:
        print("Такого столбца нет / он имеет не числовое значение / он идентичен первому столбцу!")
        continue
    break

first_column = data.iloc[:, index1 - 1].tolist()
second_column = data.iloc[:, index2 - 1].tolist()
ResultList = [first_column, second_column]

empty()
past_length = 0
while len(ResultList[0]) != past_length:
    past_length = len(ResultList[0])
    normalize()

if significance_test(correlation(), len(ResultList[0])) == 1:
    print("Корреляция:", correlation(), "(значим)")
else:
    print("Корреляция:", correlation(), "(незначим)")


# РЕГРЕССИЯ_____________________________________________________________________________________________________________

print("Введите, сколько факторов будет в модели: ")
factors = int(input())
ResultList = []

for index1 in range(factors):
    while True:
        print("Введите номер столбца для фактора", index1 + 1, ":")
        i = int(input())
        if i not in (3, 4, 6, 7, 8, 9):
            print("Такого столбца нет или он имеет не числовое значение!")
            continue
        break
    ResultList.append(data.iloc[:, i - 1].tolist())

while True:
    print("Введите номер столбца для объясняемого фактора")
    i = int(input())
    if i not in (3, 4, 6, 7, 8, 9):
        print("Такого столбца нет или он имеет не числовое значение!")
        continue
    break
ResultList.append(data.iloc[:, i - 1].tolist())

empty()

past_length = 0
while len(ResultList[0]) != past_length:  # Удаляем аномалии, пока они есть
    past_length = len(ResultList[0])
    normalize()

X = pd.DataFrame(ResultList[:-1]).T
Y = pd.DataFrame(ResultList[-1])

parameters = regress()
print(parameters)

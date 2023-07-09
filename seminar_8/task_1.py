# Даны значения величины заработной платы заемщиков банка (zp) и значения
# их поведенческого кредитного скоринга (ks): zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]. Найдите ковариацию этих двух величин
# с помощью элементарных действий, а затем с помощью функции cov из numpy Полученные значения
# должны быть равны. Найдите коэффициент корреляции Пирсона с помощью ковариации и
# среднеквадратичных отклонений двух признаков, а затем с использованием функций из библиотек numpy и pandas.
import numpy as np
import scipy.stats as stats

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
cov = np.mean(zp*ks) - np.mean(zp) * np.mean(ks)
print(cov)
# 9157.839999999997
cov1 = np.cov(zp, ks, ddof=0)
print(cov1)
# [[ 3494.64  9157.84]
#  [ 9157.84 30468.89]]
r = cov/(np.std(zp, ddof=0)*np.std(ks, ddof=0))
print(r)
# 0.8874900920739158
r1 = np.corrcoef(zp, ks)
print(r1)
# [[1.         0.88749009]
#  [0.88749009 1.        ]]
# Коэффициент корреляции равен 0,88749, что показывает достаточно сильную линейную зависимость
# поведенческого кредитного скоринга (ks) от величины заработной платы заемщиков банка
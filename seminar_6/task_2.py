# В результате 10 независимых измерений некоторой величины X, выполненных с одинаковой точностью,
# получены опытные данные: 6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1
# Предполагая, что результаты измерений подчинены нормальному закону распределения вероятностей,
# оценить истинное значение величины X при помощи доверительного интервала,
# покрывающего это значение с доверительной вероятностью 0,95
import scipy.stats as stats
import numpy as np
a = np.array([6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1])
x = np.mean(a)
D = np.var(a, ddof=1)
t = stats.t.ppf(0.975, 9)
print(x-t*np.sqrt(D/10), x+t*np.sqrt(D/10))
# Доверительный интервал равен (6.267515851415713 6.912484148584288)
# Истинное значение величины Х будет находиться в данном интервале с вероятностью 95%

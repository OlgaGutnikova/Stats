# 5) Заявляется, что партия изготавливается со средним арифметическим 2,5 см.
# Проверить данную гипотезу, если известно, что размеры изделий подчинены
# нормальному закону распределения. Объем выборки 10, уровень статистической значимости 5%
# 2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34

import numpy as np
import scipy.stats as stats

x = np.array([2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34])
m = 2.5
n = len(x)
a = 0.05
t = (np.mean(x)-m)/np.sqrt(np.var(x, ddof=1)/n)
print(t)
t1 = stats.t.ppf(0.95, 9)
t2 = stats.t.ppf(0.05, 9)
print(t1)
print(t2)
# Наблюдаемое значение t находится между значениями t1 и t2, которые означают границы нулевой гипотезы.
# Поскольку t находится в пределах нулевой гипотезы, можно считать, что партия изготавливается
# со средним арифметическим 2,5 см.

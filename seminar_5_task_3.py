# 3.Проведите тест гипотезы. Продавец утверждает, что средний вес пачки печенья составляет 200 г.
# Из партии извлечена выборка из 10 пачек. Вес каждой пачки составляет:
# 202, 203, 199, 197, 195, 201, 200, 204, 194, 190.
# Известно, что их веса распределены нормально.
# Верно ли утверждение продавца, если учитывать, что доверительная вероятность равна 99%?
# (Провести двусторонний тест.)

import numpy as np
import scipy.stats as stats
xSrednee = 200
x = np.array([202, 203, 199, 197, 195, 201, 200, 204, 194, 190])
a = 0.005
t = (np.mean(x)-xSrednee)/np.sqrt(np.var(x, ddof=1)/len(x))
print(t)
t1 = stats.t.ppf(0.005, 9)
t2 = stats.t.ppf(0.995, 9)
print(t1)
print(t2)
# Наблюдаемое значение t находится между значениями t1 и t2, которые означают границы нулевой гипотезы.
# Поскольку t находится в пределах нулевой гипотезы, можно считать, что прадавец утверждает верно и
# статистически вес упаковки равен 200 гр.

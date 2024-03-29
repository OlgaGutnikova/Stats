# Проведите тест гипотезы. Утверждается, что шарики для подшипников, изготовленные автоматическим станком,
# имеют средний диаметр 17 мм. Используя односторонний критерий с α = 0, 05,
# проверить эту гипотезу, если в выборке из n = 100 шариков средний диаметр оказался равным 17.5 мм,
# а дисперсия известна и равна 4 кв. мм.

import scipy.stats as stats
import numpy as np
x = 17
m = 17.5
a = 0.05
n = 100
d = 4
std = np.sqrt(d)
z = (x - m)/(std/np.sqrt(n))
print(z)
print(stats.norm.ppf(0.05))
# z рассчитанное = -2.5
# z табличное = -1,64485
#  Z рассчитанное попадает под альтернативную гипотезу,а значит гипотеза, что средний диаметр равен 17 мм неверна.

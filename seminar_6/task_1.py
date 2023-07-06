# Известно, что генеральная совокупность распределена нормально
# со средним квадратическим отклонением, равным 16.
# Найти доверительный интервал для оценки математического ожидания a с надежностью 0.95,
# если выборочная средняя M = 80, а объем выборки n = 256.

import scipy.stats as stats
import numpy as np
std = 16
m = 80
n = 256
z = stats.norm.ppf(0.975)
print(m-z*std/np.sqrt(n), m+z*std/np.sqrt(n))
# Доверительный интервал равен (78.04003601545995 81.95996398454005)

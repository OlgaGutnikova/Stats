# Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
# Рост матерей  178, 165, 165, 173, 168, 155, 160, 164, 178, 175
# Используя эти данные построить 95% доверительный интервал для разности среднего роста родителей и детей.
import scipy.stats as stats
import numpy as np

a = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
b = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
n1 = len(a)
n2 = len(b)
x1 = np.mean(a)
x2 = np.mean(b)
delta = x1-x2
print(delta)
D1 = np.var(a, ddof=1)
D2 = np.var(b, ddof=1)
D = (D1+D2)/2
SE = np.sqrt(D/n1 + D/n2)
t = stats.t.ppf(0.975, 18)
print(delta - t*SE, delta + t*SE)
# Проверяемая разность роста (-1.9000000000000057) находится в интервале (-10.068418034506857 6.268418034506846)
# Проходит через 0 и значит статистических значимых изменений в росте нет.

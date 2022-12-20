import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.integrate import odeint


m = 1
a = 1
omega = 1
g = 9.81
lambda_ = g / (a * omega**2)
ypsilon = a**2 * m

x_start = -5
x_end = 5
x_step = 1

y_start = -10
y_end = 10
y_step = 1

t_start = 0
t_end = 10
t_count = 1000

def f(y, t):
    alpha, w = y
    dydt = [w, m * a**2 * omega**2 / ypsilon * (math.sin(alpha) * (math.cos(alpha) - lambda_))]
    return dydt

# - - - - - - - - - - - - - - - - - - - -

'''
    np.linspace возвращает 1000 чисел от 0 до 10
    Генерирует значения t

    odeint решает дифф. уравнение численным методом
        f - система ДУ
        y0 - начальное значение y
        t - список временных интервалов для решения
'''

# Получение точек для конкретных значений y0 и dy0
def get_points(y0, dy0):
    y0 = [y0, dy0]
    t = np.linspace(t_start, t_end, t_count)
    point = odeint(f, y0, t)
    return point

for y0 in range(y_start, y_end, y_step):
    for dy0 in range(y_start, y_end, y_step):
        sol = get_points(y0, dy0)
        plt.plot(sol[:, 0], sol[:, 1], 'r')

plt.xlim([x_start, x_end])
plt.ylim([y_start, y_end])

plt.show()

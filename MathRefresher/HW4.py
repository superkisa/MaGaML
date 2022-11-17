import matplotlib.pyplot as plt
import numpy as np


def given_function(x):
    return np.sin(x**2)


def midpoint(a, b, n):
    h = (b - a)/(n - 1)
    ar = np.array([(a + i * h + a + (i - 1) * h) / 2 for i in range(1, n)])
    return np.sum(given_function(ar) * h)


def trapezoid(a, b, n):
    h = (b - a)/(n - 1)
    ar = np.array([a + i * h for i in range(n)])
    func = given_function(ar)
    return h / 2 * (func[0] + func[-1]) + h * np.sum(func[1:-1])


a = -2
b = 4
n = 6
print('Whith midpoint rule we get:', midpoint(a, b, n))
print('Whith trapezoid rule we get:', trapezoid(a, b, n))

# Data for plotting
t = np.arange(2, 101, 1)
y1 = np.array([midpoint(a, b, i) for i in t])
y2 = np.array([trapezoid(a, b, i) for i in t])

fig, ax = plt.subplots()
ax.plot(t, y1, label='midpoint rule')
ax.plot(t, y2, label='trapezoid rule')
ax.legend()

ax.set(xlabel='number of points (n)', ylabel='value of integral')
ax.grid()
plt.show()

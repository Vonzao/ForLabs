import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import random

true_a = 0.5
true_b = -1.0
true_c = 2.0
x = np.linspace(-10, 10, 50)
y = true_a * x**2 + true_b * x + true_c + np.array([random.uniform(-3, 3) for _ in range(50)])


def get_da(x, y, a, b, c):
    return (2 / len(x)) * sum(x**2 * ((a * x**2 + b * x + c) - y))


def get_db(x, y, a, b, c):
    return (2 / len(x)) * sum(x * ((a * x**2 + b * x + c) - y))


def get_dc(x, y, a, b, c):
    return (2 / len(x)) * sum((a * x**2 + b * x + c) - y)


speed = 0.0001
epochs = 10000
a0 = 0
b0 = 0
c0 = 0


def fit(x, y, speed, epochs, a0, b0, c0):
    a = a0
    b = b0
    c = c0
    a_history = [a]
    b_history = [b]
    c_history = [c]

    for _ in range(epochs):
        da = get_da(x, y, a, b, c)
        db = get_db(x, y, a, b, c)
        dc = get_dc(x, y, a, b, c)

        a = a - speed * da
        b = b - speed * db
        c = c - speed * dc

        a_history.append(a)
        b_history.append(b)
        c_history.append(c)

    return a_history, b_history, c_history


a_history, b_history, c_history = fit(x, y, speed, epochs, a0, b0, c0)
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(bottom=0.25)

scatter = ax.scatter(x, y, color='blue', label='Исходные данные')
line, = ax.plot(x, a_history[0] * x**2 + b_history[0] * x + c_history[0], 'r-', linewidth=2, label='Регрессия')
true_line, = ax.plot(x, true_a * x**2 + true_b * x + true_c, 'g--', linewidth=2, label='Истинная функция')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
ax.grid(True)


def update(val):
    epoch = int(slider.val)
    current_a = a_history[epoch]
    current_b = b_history[epoch]
    current_c = c_history[epoch]
    line.set_ydata(current_a * x**2 + current_b * x + current_c)
    fig.canvas.draw_idle()


ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03])
slider = Slider(ax_slider, 'Эпоха', 0, epochs, valinit=0, valstep=1)
slider.on_changed(update)

if __name__ == "__main__":
    plt.show()

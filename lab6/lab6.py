import math
import numpy as np
import matplotlib.pyplot as plt


# Исходная функция и её производная
def f(x):
    return math.exp(-x / 2) * math.sin(x) + x ** 2 / 10


def df(x):
    return math.exp(-x / 2) * (math.cos(x) - 0.5 * math.sin(x)) + x / 5


# Метод градиентного спуска
def gradientDescend(func=lambda x: x ** 2, diffFunc=lambda x: 2 * x,
                    x0=3, speed=0.01, epochs=100):
    xList = []
    yList = []
    x = x0

    for _ in range(epochs):
        xList.append(x)
        yList.append(func(x))
        x = x - speed * diffFunc(x)

    return xList, yList


# Визуализация
x_vals = np.linspace(-2, 3, 400)
y_vals = [f(x) for x in x_vals]

x_points, y_points = gradientDescend(f, df, x0=2, speed=0.1, epochs=50)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='f(x) = e^(-x/2)*sin(x) + x²/10')
plt.scatter(x_points, y_points, color='red', label='Точки градиентного спуска')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Градиентный спуск для функции f(x)')
plt.legend()
plt.grid(True)
plt.show()

# Определение критического значения speed
critical_speed = 0.5
print(f"Граничное значение параметра speed: ~{critical_speed}")

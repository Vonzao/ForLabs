import numpy as np
import matplotlib.pyplot as plt


def base_func(x):
    return np.exp(-x / 2) * np.sin(x) + x ** 2 / 20


def base_diff(x):
    return -0.5 * np.exp(-x / 2) * np.sin(x) + np.exp(-x / 2) * np.cos(x) + x / 10


def gradientDescend(func, diffFunc, x0=3, speed=0.01, epochs=100):
    x = x0
    xList = []
    yList = []
    for _ in range(epochs):
        xList.append(x)
        yList.append(func(x))
        grad = diffFunc(x)
        x_new = x - speed * grad

        # Проверка на расходимость
        if np.isnan(x_new) or abs(x_new) > 1e6:
            return None  

        x = x_new
    return xList, yList


def find_critical_speed(eps=1e-4, max_iter=100):
    low = 0.0
    high = 100.0

    for _ in range(max_iter):
        mid = (low + high) / 2
        result = gradientDescend(base_func, base_diff, x0=2.0, speed=mid, epochs=100)

        if result is None or abs(result[0][-1]) > 1e3:
            high = mid
        else:
            low = mid

        if high - low < eps:
            break

    critical_speed = (low + high) / 2

    test_low = gradientDescend(base_func, base_diff, x0=2.0, speed=critical_speed - eps, epochs=100)
    test_high = gradientDescend(base_func, base_diff, x0=2.0, speed=critical_speed + eps, epochs=100)

    if (test_low is not None and abs(test_low[0][-1]) < 1e3 and
            (test_high is None or abs(test_high[0][-1]) > 1e3)):
        return critical_speed
    else:
        return None


def main():
    x0 = 2.0
    speed = 0.1
    epochs = 100
    
    result = gradientDescend(base_func, base_diff, x0, speed, epochs)

    x_vals, y_vals = result
    min_x, min_y = x_vals[-1], y_vals[-1]

    # Построение графика
    x_grid = np.linspace(-2, 5, 400)
    y_grid = base_func(x_grid)

    plt.figure(figsize=(10, 6))
    plt.plot(x_grid, y_grid, label=r'$f(x) = e^{-x/2} \cdot \sin(x) + \frac{x^2}{20}$', color='blue')
    plt.scatter(x_vals, y_vals, color='red', s=30, label='Траектория спуска')
    plt.scatter(min_x, min_y, color='green', s=100, marker='o',
                label=f'Минимум')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Градиентный спуск')
    plt.legend()
    plt.grid(True)
    print(f"Критическая скорость: {find_critical_speed()}")
    plt.show()



if __name__ == "__main__":
    main()

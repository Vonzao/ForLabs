import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.kernel_ridge import KernelRidge
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
import random


def f(x):
    return np.sin(x) + 0.5 * x + np.log(np.abs(x) + 1)



x = np.linspace(-5, 5, 100)
e = np.array([random.uniform(-1, 1) for _ in range(100)])
y = f(x) + e
X = x.reshape(-1, 1)
models = {
    "Kernel Ridge": KernelRidge(alpha=1.0, kernel='rbf', gamma=0.1),
    "SVR": SVR(kernel='rbf', C=100, gamma=0.1, epsilon=0.1),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42)
}

results = {}
for name, model in models.items():
    model.fit(X, y)
    y_pred = model.predict(X)
    mse = mean_squared_error(y, y_pred)
    results[name] = {"model": model, "y_pred": y_pred, "mse": mse}


plt.figure(figsize=(15, 10))
for i, (name, result) in enumerate(results.items(), 1):
    plt.subplot(3, 1, i)
    plt.scatter(x, y, color='blue', label='Исходные точки', alpha=0.6)
    plt.plot(x, f(x), color='green', label='Исходная функция', linewidth=2)
    plt.plot(x, result["y_pred"], color='red', label='Предсказание', linewidth=2)
    plt.title(f'{name} (MSE: {result["mse"]:.4f})')
    plt.legend()
    plt.grid()

plt.tight_layout()
plt.show()

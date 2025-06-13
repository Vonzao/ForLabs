import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score



def generate_data(data_type):
    n_samples = 500
    seed = 30

    if data_type == 'Две окружности':
        data = datasets.make_circles(n_samples=n_samples, factor=0.5, noise=0.05, random_state=seed)
    elif data_type == 'Две параболы':
        data = datasets.make_moons(n_samples=n_samples, noise=0.05, random_state=seed)
    elif data_type == 'Хаотичное распределение':
        cluster_std = [1.0, 0.5]
        data = datasets.make_blobs(n_samples=n_samples, cluster_std=cluster_std, random_state=seed, centers=2)
    elif data_type == 'Точки вокруг прямых':
        x, y = datasets.make_blobs(n_samples=n_samples, random_state=170, centers=2)
        transformation = [[0.6, -0.6], [-0.4, 0.8]]
        x_aniso = np.dot(x, transformation)
        data = (x_aniso, y)
    elif data_type == 'Слабо пересекающиеся области':
        data = datasets.make_blobs(n_samples=n_samples, random_state=seed, centers=2)

    return data


def make_meshgrid(X):
    temp_x = np.linspace(X[:, 0].min() - 1, X[:, 0].max() + 1, 100)
    temp_y = np.linspace(X[:, 1].min() - 1, X[:, 1].max() + 1, 100)
    xx, yy = np.meshgrid(temp_x, temp_y)
    return xx, yy


data_types = ['Две окружности', 'Две параболы', 'Хаотичное распределение',
              'Точки вокруг прямых', 'Слабо пересекающиеся области']

classifiers = [
    ('K Nearest Neighbors', KNeighborsClassifier(n_neighbors=3)),
    ('Support Vector Machine', SVC(kernel='rbf', C=1.0)),
    ('MLP', MLPClassifier(hidden_layer_sizes=(64, 32), activation='relu',
                          solver='adam', max_iter=1000, random_state=42))
]

fig, axes = plt.subplots(len(data_types), len(classifiers), figsize=(14, 14))
plt.subplots_adjust(hspace=0.2, wspace=0.2)

for row, data_type in enumerate(data_types):
    X, y = generate_data(data_type)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    xx, yy = make_meshgrid(X)

    for col, (clf_name, clf) in enumerate(classifiers):
        ax = axes[row, col]

        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        if hasattr(clf, "decision_function"):
            Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
        else:
            Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
        Z = Z.reshape(xx.shape)

        if hasattr(clf, "decision_function"):
            ax.contourf(xx, yy, Z, levels=np.linspace(Z.min(), Z.max(), 10), alpha=0.3, cmap='bwr')
            ax.contour(xx, yy, Z, levels=[0], linewidths=2, colors='black')
        else:
            ax.contourf(xx, yy, Z, levels=[0, 0.5, 1], alpha=0.3, cmap='bwr')
            ax.contour(xx, yy, Z, levels=[0.5], linewidths=2, colors='black')

        ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='bwr', alpha=0.5, edgecolors='k')
        ax.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, cmap='bwr', alpha=1.0, edgecolors='k', linewidths=1)

        incorrect = (y_pred != y_test)
        ax.scatter(X_test[incorrect, 0], X_test[incorrect, 1], c='black', marker='x', s=100)

        if row == 0:
            ax.set_title(clf_name, pad=20, fontsize=12)
        if col == 0:
            ax.set_ylabel(data_type, rotation=90, size=12, labelpad=20)

plt.tight_layout()
plt.show()

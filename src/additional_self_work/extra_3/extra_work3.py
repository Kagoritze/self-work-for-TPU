import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider


# Функция для инициализации центроидов
def initialize_centroids(X, k):
    return X[np.random.choice(X.shape[0], k, replace=False)]


# Функция для присвоения кластеров
def assign_clusters(X, centroids):
    distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)
    return np.argmin(distances, axis=1)


# Функция для обновления центроидов
def update_centroids(X, labels, k):
    return np.array([X[labels == i].mean(axis=0) for i in range(k)])


# Основная функция K-средних
def k_means(X, k, max_iters=100):
    centroids = initialize_centroids(X, k)
    history = []  # Список для хранения истории центроидов и меток
    for _ in range(max_iters):
        labels = assign_clusters(X, centroids)
        history.append((centroids.copy(), labels.copy()))  # Сохраняем текущее состояние
        new_centroids = update_centroids(X, labels, k)
        if np.all(centroids == new_centroids):  # Проверка на сходимость
            break
        centroids = new_centroids
    return history


# Генерация случайных данных
np.random.seed(42)
X = np.vstack(
    [np.random.normal(loc, 0.5, (100, 2)) for loc in [(2, 2), (8, 8), (5, 1)]]
)

# Применение K-средних
k = 3
history = k_means(X, k)

# Подготовка графика
fig, ax = plt.subplots(figsize=(8, 6))
plt.subplots_adjust(bottom=0.25)
line_clusters = [ax.scatter([], [], label=f"Cluster {i+1}") for i in range(k)]
centroid_scatter = ax.scatter(
    [], [], color="black", marker="X", s=200, label="Centroids"
)
ax.set_title("K-means Clustering")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.legend()
ax.grid()

# Создание ползунка
slider_ax = plt.axes([0.2, 0.1, 0.65, 0.03])  # [left, bottom, width, height]
slider = Slider(slider_ax, "Iteration", 0, len(history) - 1, valinit=0, valstep=1)


# Функция для обновления графика
def update_plot(val):
    iteration = int(slider.val)
    centroids, labels = history[iteration]
    for i in range(k):
        line_clusters[i].set_offsets(X[labels == i])
    centroid_scatter.set_offsets(centroids)


slider.on_changed(update_plot)

# Первоначальное обновление графика
update_plot(0)

plt.show()

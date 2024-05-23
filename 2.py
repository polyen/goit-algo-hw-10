import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi
from monte_carlo import monte_carlo_simulation


def f(x):
    return x ** 3


def create_chart():
    a = 0  # Нижня межа
    b = 2  # Верхня межа

    # Створення діапазону значень для x
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = x^3 від ' + str(a) + ' до ' + str(b))
    plt.grid()
    plt.show()


def accurate_integral():
    # Визначте межі інтегрування, наприклад, від 0 до 1
    a = 0  # нижня межа
    b = 2  # верхня межа

    # Обчислення інтеграла
    result, error = spi.quad(f, a, b)

    return result


def by_monte_carlo(num_experiments):
    a = 2
    b = 8

    return monte_carlo_simulation(a, b, num_experiments)


if __name__ == "__main__":
    create_chart()
    acc = accurate_integral()

    num_experiments = 100
    mc = by_monte_carlo(num_experiments)

    print(f"Теоретична площа фігури: {acc}")
    print(f"Середня площа трикутника за {num_experiments} експериментів: {mc}")

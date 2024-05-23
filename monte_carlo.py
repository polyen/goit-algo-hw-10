import random


def is_inside(x, y):
    return y <= x ** 3


def monte_carlo_simulation(a, b, num_experiments):
    average_area = 0

    for _ in range(num_experiments):
        points = [(random.uniform(0, a), random.uniform(0, b)) for _ in range(15000)]
        inside_points = [point for point in points if is_inside(point[0], point[1])]

        M = len(inside_points)
        N = len(points)
        area = (M / N) * (a * b)

        average_area += area

    average_area /= num_experiments
    return average_area


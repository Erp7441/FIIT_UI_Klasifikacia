from random import uniform, choice

from utils.Constants import AMOUNT_OF_POINTS


def generate_initial_points():
    initial_points = {
        'R': [(-4500, -4400), (-4100, -3000), (-1800, -2400), (-2500, -3400), (-2000, -1400)],
        'G': [(4500, -4400), (4100, -3000), (1800, -2400), (2500, -3400), (2000, -1400)],
        'B': [(-4500, 4400), (-4100, 3000), (-1800, 2400), (-2500, 3400), (-2000, 1400)],
        'P': [(4500, 4400), (4100, 3000), (1800, 2400), (2500, 3400), (2000, 1400)]
    }
    return initial_points


def generate_test_points(amount_of_points=AMOUNT_OF_POINTS):
    test_points = []
    test_colors = []

    for _ in range(amount_of_points):
        x = uniform(-5000, 5000)
        y = uniform(-5000, 5000)

        if x < 500 and y < 500:
            color = 'R'
        elif x > -500 and y < 500:
            color = 'G'
        elif x < 500 and y > -500:
            color = 'B'
        elif x > -500 and y > -500:
            color = 'P'
        else:
            color = choice(['R', 'G', 'B', 'P'])

        test_points.append((x, y))
        test_colors.append(color)

    return test_points, test_colors

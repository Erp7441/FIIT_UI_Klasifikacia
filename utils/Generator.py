from random import uniform, choice

from classifier.Point import Point
from utils.Constants import AMOUNT_OF_POINTS
from utils.Timer import Timer
from utils.Utils import print_color


def generate_initial_points(return_type: type = dict):
    initial_points = {
        'R': [Point(-4500, -4400, 'R'), Point(-4100, -3000, 'R'), Point(-1800, -2400, 'R'), Point(-2500, -3400, 'R'), Point(-2000, -1400, 'R')],
        'G': [Point(4500, -4400, 'G'), Point(4100, -3000, 'G'), Point(1800, -2400, 'G'), Point(2500, -3400, 'G'), Point(2000, -1400, 'G')],
        'B': [Point(-4500, 4400, 'B'), Point(-4100, 3000, 'B'), Point(-1800, 2400, 'B'), Point(-2500, 3400, 'B'), Point(-2000, 1400, 'B')],
        'P': [Point(4500, 4400, 'P'), Point(4100, 3000, 'P'), Point(1800, 2400, 'P'), Point(2500, 3400, 'P'), Point(2000, 1400, 'P')],
    }

    if return_type is list:
        return initial_points['R'] + initial_points['G'] + initial_points['B'] + initial_points['P']
    else:
        return initial_points


def generate_point():
    x = uniform(-5000, 5000)
    y = uniform(-5000, 5000)
    color = None

    probability = uniform(0, 1)
    if probability < 0.99:
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

    return Point(x, y, color)


def generate_test_points(amount_of_points=None):
    if amount_of_points is None:
        amount_of_points = AMOUNT_OF_POINTS

    # TODO:: Check if the generated points are unique
    test_points = []

    for _ in range(amount_of_points):
        point = generate_point()

        # Two points generated right after each other should not have the same color
        if len(test_points) != 0 and point.color == test_points[-1].color:
            while point.color == test_points[-1].color:
                point = generate_point()

        test_points.append(point)

    return test_points


def generate_test_points_with_measurement(amount_of_testing_points: int = None):
    timer = Timer()

    print_color("\nGenerating testing points...", color="blue")
    timer.start()

    # Generating test points
    test_points = generate_test_points(amount_of_testing_points)

    timer.stop()
    print_color("{0} Testing points generated in {1} seconds".format(len(test_points), timer.elapsed_time), color="green")

    return test_points

from matplotlib import pyplot as plt

from utils.Constants import DEFAULT_K
from utils.Generator import generate_initial_points


class Classifier:
    def __init__(self, k=None, initial_points=None):
        self.points = {'R': [], 'G': [], 'B': [], 'P': []}

        if initial_points is None:
            # Generating starting points
            self.initial_points = generate_initial_points()
        else:
            self.initial_points = initial_points

        # Adding initial points to the space
        for color, points in self.initial_points.items():
            for point in points:
                self.add_point(point[0], point[1], color)

        if k is None:
            self.k = DEFAULT_K
        else:
            self.k = k

        # TODO:: Visualize initial points?

    def add_point(self, x, y, color):
        self.points[color].append((x, y))

    def classify(self, x, y):
        # Finding nearest neighbors
        neighbors = self.find_neighbors(x, y)

        # Class determination based on the majority of neighbours
        class_count = {'R': 0, 'G': 0, 'B': 0, 'P': 0}
        for neighbor in neighbors:
            for color, points in self.points.items():
                if neighbor in points:
                    class_count[color] += 1

        max_class = max(class_count, key=class_count.get)
        self.add_point(x, y, max_class)  # Add a classified point to the space
        return max_class

    def find_neighbors(self, x, y):
        # Dividing the space into smaller squares
        grid_size = 1000
        grid = {}
        for color, points in self.points.items():
            grid[color] = {}
            for point in points:
                grid_x, grid_y = point[0] // grid_size, point[1] // grid_size
                if (grid_x, grid_y) not in grid[color]:
                    grid[color][(grid_x, grid_y)] = []
                grid[color][(grid_x, grid_y)].append(point)

        # Search for neighbours near a classified point
        neighbors = []

        # Getting x and y coordinates relative to the grid
        grid_x, grid_y = x // grid_size, y // grid_size
        for i in range(-1, 2):
            for j in range(-1, 2):
                current_grid = (
                    grid.get('R', {}).get((grid_x + i, grid_y + j), []) +
                    grid.get('G', {}).get((grid_x + i, grid_y + j), []) +
                    grid.get('B', {}).get((grid_x + i, grid_y + j), []) +
                    grid.get('P', {}).get((grid_x + i, grid_y + j), [])
                )
                neighbors.extend(current_grid)

        # Returning k nearest neighbours
        return sorted(neighbors, key=lambda p: ((p[0] - x) ** 2 + (p[1] - y) ** 2))[:self.k]

    def visualize(self, test_points, title=None):
        colors = {'R': 'red', 'G': 'green', 'B': 'blue', 'P': 'purple'}

        # Visualize each point in a scatter plot
        for color, points in self.points.items():
            x_vals = [point[0] for point in points]
            y_vals = [point[1] for point in points]
            plt.scatter(x_vals, y_vals, color=colors[color], label=color)

        # Visualize empty points
        x_empty = [point[0] for point in test_points if self.classify(point[0], point[1]) == '']
        y_empty = [point[1] for point in test_points if self.classify(point[0], point[1]) == '']
        plt.scatter(x_empty, y_empty, color='gray', label='Empty')

        plt.legend()

        if title is None:
            title = "Visualization of the 2D space with k={0} and t={1}".format(self.k, len(test_points))

        plt.title(title)
        plt.show()

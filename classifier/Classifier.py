from matplotlib import pyplot as plt

from classifier.Point import Point
from utils.Constants import DEFAULT_K, PROGRESS_PERCENTAGE_STEP, GRID_SIZE, SEARCH_SIZE, UNCLASSIFIED_POINT_COLOR, \
    UNCLASSIFIED_POINT_LABEL
from utils.Generator import generate_initial_points


class Classifier:
    def __init__(self, k=None):
        self.points = {'R': [], 'G': [], 'B': [], 'P': []}
        self.initial_points = generate_initial_points(list)

        self._all_points = []
        self._all_classified_points = []
        self._all_unclassified_points = []

        # Adding initial points to the space
        for point in self.initial_points:
            self.add_point_o(point)

        if k is None:
            self.k = DEFAULT_K
        else:
            self.k = k

    def add_point(self, x, y, color):
        point = Point(x, y, color)
        self._all_points.append(point)
        self.points[color].append(point)
        self._all_classified_points.append(point)
        return point

    def add_point_o(self, point: Point):
        self._all_points.append(point)
        self.points[point.color].append(point)
        self._all_classified_points.append(point)
        return point

    def add_unclassified_point(self, x, y):
        point = Point(x, y)
        self._all_points.append(point)
        self._all_unclassified_points.append(point)
        return point

    def classify(self, x, y):
        # Finding nearest neighbors
        neighbors = self.find_neighbors(x, y)

        # If no neighbors were found. Point cannot be classified.
        if neighbors is None or len(neighbors) == 0:
            return self.add_unclassified_point(x, y)

        # Class determination based on the majority of neighbours
        class_count = {'R': 0, 'G': 0, 'B': 0, 'P': 0}
        for neighbor in neighbors:
            class_count[neighbor.color] += 1

        max_class = max(class_count, key=class_count.get)
        return self.add_point(x, y, max_class)  # Add a classified point to the space

    def classify_with_progress(self, test_points: [] = None, percentage_step=None):
        if test_points is None:
            return None

        if percentage_step is None:
            percentage_step = PROGRESS_PERCENTAGE_STEP

        total_points = len(test_points)
        progress_step = total_points // (100 // percentage_step)

        for i in range(total_points):
            point = self.classify(test_points[i].x, test_points[i].y)
            point.parent_index = i  # For calculating success rate of classification

            if (i + 1) % progress_step == 0:
                progress = ((i + 1) / total_points) * 100
                print(f"Status: {progress:.0f}%")

    def find_neighbors(self, x, y):
        neighbors = []

        # Getting x and y coordinates relative to the grid (shrinking the x and y values)
        target_grid_x, target_grid_y = x // GRID_SIZE, y // GRID_SIZE

        # Search for neighbours near a classified point within a GRID_SIZE radius (nearest shrink value to the main one)
        for point in self._all_classified_points:
            grid_x, grid_y = point.x // GRID_SIZE, point.y // GRID_SIZE

            # Search if point falls within x times x subgrid (relative grid values of x and y)
            if (
                (grid_x - SEARCH_SIZE <= target_grid_x <= grid_x + SEARCH_SIZE) and
                (grid_y - SEARCH_SIZE <= target_grid_y <= grid_y + SEARCH_SIZE)
            ):
                neighbors.append(point)

        # Returning k nearest neighbours (Sorting by Pytagoras theorem)
        return sorted(neighbors, key=lambda p: ((p.x - x) ** 2 + (p.y - y) ** 2))[:self.k]

    def visualize(self, test_points, title=None):
        colors = {'R': 'red', 'G': 'green', 'B': 'blue', 'P': 'purple'}

        # Visualize points color by color
        for color, points in self.points.items():
            x_vals = [point.x for point in points]
            y_vals = [point.y for point in points]
            plt.scatter(x_vals, y_vals, color=colors[color], label=color)

        # Visualize empty points with gray color
        x_empty = [point.x for point in self._all_unclassified_points]
        y_empty = [point.y for point in self._all_unclassified_points]
        plt.scatter(x_empty, y_empty, color=UNCLASSIFIED_POINT_COLOR, label=UNCLASSIFIED_POINT_LABEL)

        plt.legend()

        if title is None:
            title = "Visualization of the 2D space with k={0} and t={1}".format(self.k, len(test_points))

        plt.title(title)
        plt.show()

    def get_success_rate(self, test_points: [] = None):
        if test_points is None:
            return None

        all_points_except_initials = [point for point in self._all_points if point not in self.initial_points]
        classified = {
            "Correctly": 0,
            "Incorrectly": 0
        }

        for point in all_points_except_initials:
            if point.color == test_points[point.parent_index].color:
                classified["Correctly"] += 1
            else:
                classified["Incorrectly"] += 1

        # Success rate %
        success_rate = (100 * classified["Correctly"]) / (classified["Correctly"] + classified["Incorrectly"])

        return classified, success_rate

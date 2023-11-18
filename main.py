from classifier.Classifier import Classifier
from utils.Args import Args
from utils.Generator import generate_test_points

if __name__ == '__main__':
    args = Args()
    classifier = Classifier()

    # Generate testing points
    if args.amount_of_testing_points is not None:
        test_points, test_colors = generate_test_points(args.amount_of_testing_points)
    else:
        test_points, test_colors = generate_test_points()

    if args.k is not None:
        for i in range(len(test_points)):
            classifier.classify(test_points[i][0], test_points[i][1], args.k)
    else:
        for i in range(len(test_points)):
            classifier.classify(test_points[i][0], test_points[i][1])

    # Visualization of the resulting 2D space
    classifier.visualize(test_points)

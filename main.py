from classifier.Classifier import Classifier
from utils.Args import Args
from utils.Generator import generate_test_points

if __name__ == '__main__':
    args = Args()
    classifier = Classifier(args.k)

    # Generate testing points
    test_points, test_colors = generate_test_points(args.amount_of_testing_points)
    for i in range(len(test_points)):
        classifier.classify(test_points[i][0], test_points[i][1])

    # Visualization of the resulting 2D space
    classifier.visualize(test_points)

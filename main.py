from utils.Args import Args
from utils.Generator import generate_test_points_with_measurement
from classifier.ClassifierMeasure import run_creation_measurement, run_classify_measurement

# TODO:: Add colors to output


def main():
    args = Args()

    test_points = generate_test_points_with_measurement(args.amount_of_testing_points)

    if args.tests:
        run_tests(test_points)
        return

    classifier = run_creation_measurement(args.k)
    run_classify_measurement(classifier, test_points)


def run_tests(test_points: [] = None):

    classifiers = [
        run_creation_measurement(1), run_creation_measurement(3),
        run_creation_measurement(7), run_creation_measurement(15)
    ]

    for classifier in classifiers:
        run_classify_measurement(classifier, test_points)


if __name__ == '__main__':
    main()

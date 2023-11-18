from classifier.Classifier import Classifier
from utils.Args import Args
from utils.Generator import generate_test_points
from utils.Timer import Timer

# TODO:: Add colors to output
# TODO:: Add argument to change initial points
# TODO:: Compare the return value of the classify function with the generated point. Based on these comparisons, evaluate the success of your classifier for the experiment.


def main():
    args = Args()
    timer = Timer()

    if args.tests:
        run_tests()
        return

    print("Creating classifier...")
    timer.start()

    # Creating classifier
    classifier = Classifier(args.k)

    timer.stop()
    print("Classifier created in {0} seconds".format(timer.elapsed_time))

    run_classifier_measurement(classifier, args.amount_of_testing_points)


def run_tests(args: Args = None):
    timer = Timer()

    ###########################################################################
    print("Creating classifier...")
    timer.start()

    # Creating classifier
    classifier1 = Classifier(1)
    classifier3 = Classifier(3)
    classifier7 = Classifier(7)
    classifier15 = Classifier(15)

    timer.stop()
    print("Classifier created in {0} seconds".format(timer.elapsed_time))

    amount_of_testing_points = None if args is None else args.amount_of_testing_points
    for classifier in [classifier1, classifier3, classifier7, classifier15]:
        run_classifier_measurement(classifier, amount_of_testing_points)


def run_classifier_measurement(classifier: Classifier, amount_of_testing_points=None):
    timer = Timer()

    print("\nRunning measurement on k = {0} classifier...".format(classifier.k))

    ###########################################################################
    print("\nGenerating testing points...")
    timer.start()

    # Generating test points
    # TODO:: Adapt test_colors according to the task.
    test_points, test_colors = generate_test_points(amount_of_testing_points)

    timer.stop()
    print("{0} Testing points generated in {1} seconds".format(len(test_points), timer.elapsed_time))

    ###########################################################################
    print("\nClassifying testing points...")
    timer.start()

    # Classifying test points
    classifier.classify_with_progress(test_points)

    timer.stop()
    print("{0} Testing points classified in {1} seconds".format(len(test_points), timer.elapsed_time))

    ###########################################################################
    print("\nVisualizing the result of the 2D space...")
    timer.start()

    # Visualization of the resulting 2D space
    classifier.visualize(test_points)

    timer.stop()
    print("Visualization finished in {0} seconds".format(timer.elapsed_time))


if __name__ == '__main__':
    main()

from classifier.Classifier import Classifier
from utils.Constants import ROUNDING_PRECISION, GOOD_SUCCESS_RATE, BAD_SUCCESS_RATE
from utils.Timer import Timer
from utils.Utils import print_color, print_percentage


def run_classify_measurement(classifier: Classifier, test_points: [] = None):
    print_color("\nRunning measurement on k = {0} classifier...".format(classifier.k), color="purple")

    timer = Timer()

    print_color("\nClassifying testing points...", color="blue")
    timer.start()

    # Classifying test points
    classifier.classify_with_progress(test_points)

    timer.stop()
    print_color("{0} Testing points classified in {1} seconds".format(len(test_points), timer.elapsed_time), color="green")

    run_visualization_measurement(classifier, test_points)

    # Statistics
    classifier_count, classifier_success_rate = classifier.get_success_rate(test_points)
    test_points_length = len(test_points)

    print_color("\nCorrectly classified {0} of {1} points".format(classifier_count["Correctly"], test_points_length), color="green")
    print_color("Incorrectly classified {0} of {1} points".format(classifier_count["Incorrectly"], test_points_length), color="red")

    rounded_percentage = round(classifier_success_rate, ROUNDING_PRECISION)
    print_percentage(
    "Success rate: {0}%".format(rounded_percentage),
        percentage=classifier_success_rate, good=GOOD_SUCCESS_RATE, bad=BAD_SUCCESS_RATE
    )


def run_creation_measurement(k: int = None):
    timer = Timer()

    print_color("Creating classifier...", color="blue")
    timer.start()

    # Creating classifier
    classifier = Classifier(k)

    timer.stop()
    print_color("Classifier k = {0} created in {1} seconds".format(classifier.k, timer.elapsed_time), color="green")

    return classifier


def run_visualization_measurement(classifier: Classifier, test_points: [] = None):
    timer = Timer()

    print_color("\nVisualizing the result of the 2D space...", color="blue")
    timer.start()

    # Visualization of the resulting 2D space
    classifier.visualize(test_points)

    timer.stop()
    print_color("Visualization finished in {0} seconds".format(timer.elapsed_time), color="green")

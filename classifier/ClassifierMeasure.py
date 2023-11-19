from classifier.Classifier import Classifier
from utils.Timer import Timer


def run_classify_measurement(classifier: Classifier, test_points: [] = None):
    print("\nRunning measurement on k = {0} classifier...".format(classifier.k))

    timer = Timer()

    print("\nClassifying testing points...")
    timer.start()

    # Classifying test points
    classifier.classify_with_progress(test_points)

    timer.stop()
    print("{0} Testing points classified in {1} seconds".format(len(test_points), timer.elapsed_time))

    run_visualization_measurement(classifier, test_points)


def run_creation_measurement(k: int = None):
    timer = Timer()

    print("Creating classifier...")
    timer.start()

    # Creating classifier
    classifier = Classifier(k)

    timer.stop()
    print("Classifier k = {0} created in {1} seconds".format(classifier.k, timer.elapsed_time))

    return classifier


def run_visualization_measurement(classifier: Classifier, test_points: [] = None):
    timer = Timer()

    print("\nVisualizing the result of the 2D space...")
    timer.start()

    # Visualization of the resulting 2D space
    classifier.visualize(test_points)

    timer.stop()
    print("Visualization finished in {0} seconds".format(timer.elapsed_time))
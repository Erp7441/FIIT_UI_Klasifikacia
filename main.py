from classifier.Classifier import Classifier
from utils.Args import Args
from utils.Generator import generate_test_points
from utils.Timer import Timer

# TODO:: Add colors to output

if __name__ == '__main__':
    args = Args()
    timer = Timer()

    ###########################################################################
    print("Creating classifier...")
    timer.start()

    # Creating classifier
    classifier = Classifier(args.k)

    timer.stop()
    print("Classifier created in {0} seconds".format(timer.elapsed_time))

    ###########################################################################
    print("Generating testing points...")
    timer.start()

    # Generating test points
    test_points, test_colors = generate_test_points(args.amount_of_testing_points)

    timer.stop()
    print("{0} Testing points generated in {1} seconds".format(len(test_points), timer.elapsed_time))

    ###########################################################################
    print("Classifying testing points...")
    timer.start()

    # Classifying test points
    for i in range(len(test_points)):
        classifier.classify(test_points[i][0], test_points[i][1])

    timer.stop()
    print("{0} Testing points classified in {1} seconds".format(len(test_points), timer.elapsed_time))

    ###########################################################################
    print("Visualizing the result of the 2D space...")
    timer.start()

    # Visualization of the resulting 2D space
    classifier.visualize(test_points)

    timer.stop()
    print("Visualization finished in {0} seconds".format(timer.elapsed_time))

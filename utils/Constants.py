AMOUNT_OF_POINTS = 40000  # Amount of testing points to be generated (default value)
DEFAULT_K = 1
GRID_SIZE = 1000  # Size of the x times x grid where to look for neighbors. (shrinking x and y values)
SUB_GRID_SIZE = 3  # Subgrid of the neighbor grid. We look for neighbor points within this subgrid.
PROGRESS_PERCENTAGE_STEP = 10

UNCLASSIFIED_POINT_COLOR = 'gray'
UNCLASSIFIED_POINT_LABEL = 'Empty'
GOOD_SUCCESS_RATE = 85  # % (or higher)
BAD_SUCCESS_RATE = 80  # % (or lower)

ROUNDING_PRECISION = 3

DEBUG = True

SEARCH_SIZE = SUB_GRID_SIZE // 2  # Search size for nearest neighbors

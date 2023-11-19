from datetime import datetime

from utils.Constants import DEBUG


def print_debug(*args, **kwargs):
    if DEBUG:
        timestamp = datetime.now().strftime("%H:%M:%S")
        prefix = f"DEBUG [{timestamp}]: "
        message = " ".join(str(arg) for arg in args)
        print(prefix + message, **kwargs)


# Prints out text in color
def print_color(*args, color="white", **kwargs):
    color_codes = {
        'black': '30',
        'red': '31',
        'green': '32',
        'yellow': '33',
        'blue': '34',
        'purple': '35',
        'cyan': '36',
        'white': '37'
    }

    if color not in color_codes:
        raise ValueError(f"Invalid color: {color}")

    color_code = color_codes[color]
    message = " ".join(str(arg) for arg in args)
    print(f"\033[{color_code}m{message}\033[0m", **kwargs)


# Percentage functions
def get_percentage_color(percentage, good_percentage, bad_percentage):
    if percentage <= bad_percentage:
        return "red"
    elif percentage >= good_percentage:
        return "green"
    else:
        return "yellow"


def print_percentage(*args, percentage, good, bad, **kwargs):
    color = get_percentage_color(percentage, good, bad)
    print_color(*args, color=color, **kwargs)
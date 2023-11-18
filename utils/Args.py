import os
import signal

from utils.ArgsParser import ArgsParser


class Args:

    def __init__(self):
        # Parsing arguments
        self.parser = ArgsParser(
            description="UI Classificator by Martin Szabo",

        )

        general_group = self.parser.add_argument_group("General")
        general_group.add_argument("--amount-of-neighbors", "-k", type=int, dest="k", help="Amount of neighbors to look for")
        general_group.add_argument("--amount-of-testing-points", "-t", type=int, dest="amount_of_testing_points", help="Amount of testing points to generate")

        args_dict = self.parser.parse_args().__dict__

        for k, v in args_dict.items():
            setattr(self, k, v)

    def parse_int(self, arg, default_value):
        value = self._convert_arg_to_int(arg)
        value = value if value is not None else default_value
        return value

    def _convert_arg_to_int(self, arg):
        if arg is not None:
            try:
                return int(arg)
            except ValueError:
                print("Could not convert argument value \"{}\" to integer value!".format(arg))
                if not self._get_confirmation():
                    pid = os.getpid()
                    os.kill(pid, signal.SIGTERM)
                print("Using default value...\n")
                return None

    @staticmethod
    def _get_confirmation():
        response = ''
        while response != 'Y' and response != 'N':
            print("Do you wish to continue? (y/n): ", end='')
            response = input().upper()
        return response == 'Y'
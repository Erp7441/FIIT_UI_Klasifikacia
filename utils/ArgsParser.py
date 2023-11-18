from argparse import ArgumentParser


class ArgsParser(ArgumentParser):
    def format_help(self):
        default_help = super().format_help()
        custom_help = """\n

"""
        return default_help + custom_help

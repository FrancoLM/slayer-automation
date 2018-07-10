import sys


class SysStdoutLogger(object):
    """sys.stdout logger class

    This class duplicates the console output and saves it to a file, in order to consolidate
    the behave and slayer logs.
    This class is meant to overwrite the sys.stdout output"""

    def __init__(self, filename="slayer.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "w")

    def __getattr__(self, attr):
        return getattr(self.terminal, attr)

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

import sys
from io import StringIO


class OutputCapturer:
    def __init__(self):
        self.output = ""
        self.buffer = None
        self.original_stdout = None

    def start(self):
        self.original_stdout = sys.stdout
        sys.stdout = self.buffer = StringIO()

    def stop(self):
        self.output += self.buffer.getvalue()
        sys.stdout = self.original_stdout

    def get_output(self):
        return self.output

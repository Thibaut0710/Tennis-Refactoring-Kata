from io import StringIO


class StringBuilderConsole:
    def __init__(self):
        self.output = StringIO()

    def write(self, message):
        self.output.write(message + "\n")

    def get_output(self):
        return self.output.getvalue()
from qasm.error.RuntimeError import RuntimeError


class ParseError(RuntimeError):

    def __init__(self, token, message):
        super().__init__(token, message)

    def report(self):
        return "[ERROR] Error: QASMParseError, Response: ({0})".format(super().report())

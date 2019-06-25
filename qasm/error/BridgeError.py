from qasm.error.RuntimeError import RuntimeError


class BridgeError(RuntimeError):

    def __init__(self, token, message):
        super().__init__(token, message)

    def report(self):
        return "[ERROR] Error: QASMBridgeError, Response: ({0})".format(super().report())
class RuntimeError(Exception):

    def __init__(self, token, message):
        """
        Runtime Error constructor

        :param token: token that raised the error (aqa_assembly_simulator.lexer.Token.Token)
        :param message: error message (string)
        """

        self._token = token
        self._message = message

    def report(self):
        """
        Report method. Used to produce a string representation of the error when the error is printed.

        :return: (string)
        """

        return "Line: {0}, Where: {1},  Message: {2}.".format(
            self._token.get_line(), self._token.get_lexeme(), self._message
        )

    __repr__ = report

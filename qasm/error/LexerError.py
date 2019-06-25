class LexerError(Exception):

    def __init__(self, line, message, character):
        """
        Lexer Error constructor

        :param line: line that the error occurs in the plain text (integer)
        :param message: error message (string)
        :param character: character that raised the error (string)
        """

        self._line = line
        self._message = message
        self._character = character

    def report(self):
        """
        Report method. Used to produce a string representation of the error when the error is printed.

        :return: (string)
        """

        return "[ERROR] Error: QASMLexerError, Response: (Line: {0}, Message: {1}, Character: {2})".format(
            self._line, self._message, self._character
        )

    __repr__ = report

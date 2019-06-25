class Token:

    def __init__(self, type, lexeme, literal, line):
        """
        Token constructor

        :param type: token type (qasm.lexer.TokenType.TokenType)
        :param lexeme: string representation of the token (string)
        :param literal: literal of the token
        :param line: (integer)
        """

        self._type = type
        self._lexeme = lexeme
        self._literal = literal
        self._line = line

    def get_type(self):
        """
        Returns the token type

        :return: (qasm.lexer.TokenType.TokenType)
        """

        return self._type

    def get_lexeme(self):
        """
        Return the string representation of the token

        :return: (string)
        """

        return self._lexeme

    def get_literal(self):
        """
        Returns literal of the token

        :return:
        """

        return self._literal

    def get_line(self):
        """
        Returns the line of the token

        :return: (integer)
        """

        return self._line

    def __str__(self):
        """
        Returns user friendly string representation of the token object

        :return: (string)
        """

        return self._lexeme

    def __repr__(self):
        """
        Returns the string representation of the token object (Debug)

        :return: (string)
        """

        return "(Type: {0}, Lexeme: {1}, Literal: {2})".format(
            self._type, self._lexeme, self._literal
        )

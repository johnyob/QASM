import json

from qasm.lexer.TokenType import TokenType, STATEMENTS
from qasm.helpers.Constants import SYNTAX_JSON
from qasm.error.ParseError import ParseError
from qasm.helpers.Util import read_file


class Parser:

    def __init__(self, tokens):
        """
        Parser (syntactic analyser) constructor

        :param tokens: list containing tokens produced from lexical analysis (list)
        """

        self._current = 0
        self._tokens = tokens

        self._syntax = self._read_syntax()
        self._errors = []

    def get_errors(self):
        """
        Returns internal parser errors

        :return: (list)
        """

        return self._errors

    def _read_syntax(self):
        """
        Returns syntax conditions stored in syntax.json.
        Converts keys from string to integer.

        :return: (dict)
        """

        return {
            int(key): value for key, value
            in json.loads(read_file(SYNTAX_JSON)).items()
        }

    def parse(self):
        """
        Performs syntactic analysis on the tokens to produce a list of statements.

        :return: (list)
        """

        statements = []

        while not self._is_at_end():
            statements.append(self._statement())

        return statements

    def _statement(self):
        """
        Parses tokens to statement.
        Uses syntax conditions stored in syntax.json to parse tokens to valid statements.
        If an unexpected token is discovered then a parser error is raised.

        :return: (qasm.parser.Statement.Statement)
        """

        try:
            if self._match(TokenType.MEASURE):
                return STATEMENTS[11](self._previous())

            for type in self._syntax.keys():
                   if self._match(TokenType(type)):
                       return self._instruction(type)

            raise self._error(self._peek(), "Unexpected token")
        except ParseError:
            self._synchronise()
            return None

    def _instruction(self, type):
        """
        Uses syntax conditions for :param type to parse current tokens to statement.
        If unexpected token is discovered then a parser error is raised.

        :param type: token type (integer)
        :return: (qasm.parser.Statement.Statement)
        """

        tokens = []

        for token in self._syntax[type]:
            if TokenType(token["Type"]) == TokenType.COMMA:
                self._consume(TokenType.COMMA, token["Error"])
            else:
                tokens.append(self._consume(TokenType(token["Type"]), token["Error"]))

        return STATEMENTS[type](tokens)

    def _consume(self, type, message):
        """
        Consumes current token if expected token is found, otherwise raise parser error

        :param type: expected token type (qasm.lexer.TokenType.TokenType)
        :param message: error message (string)
        :return: (qasm.lexer.Token.Token)
        """

        if self._check(type):
            return self._move()

        raise self._error(self._peek(), message)

    def _match(self, type):
        """
        Matches current token to expected token type. If expected token type found, then move one token along and
        return true, otherwise return false.

        :param type: expected token type (qasm.lexer.TokenType.TokenType)
        :return: (boolean)
        """

        if self._check(type):
            self._move()
            return True

        return False

    def _check(self, type):
        """
        Checks current token against expected token type. If at end of token list then return false.
        Otherwise return whether current token type equals expected token type.

        :param type: expected token type (qasm.lexer.TokenType.TokenType)
        :return: (boolean)
        """

        if self._is_at_end():
            return False

        return self._peek().get_type() == type

    def _move(self):
        """
        Increments current pointer for tokens list, if not at the end of tokens list.
        Returns the previous token.

        :return: (qasm.lexer.Token.Token)
        """

        if not self._is_at_end():
            self._current += 1

        return self._previous()

    def _error(self, token, message):
        """
        Constructs a parser error and appends it to the internal errors list.
        Returns constructed parser error.

        :param token: token that raised the error (qasm.lexer.Token.Token)
        :param message: error message (string)
        :return: (qasm.error.ParseError.ParseError)
        """

        self._errors.append(ParseError(token, message))
        return self._errors[-1]

    def _peek(self):
        """
        Returns the current token

        :return: (qasm.lexer.Token.Token)
        """

        return self._tokens[self._current]

    def _previous(self):
        """
        Returns the previous token

        :return: (qasm.lexer.Token.Token)
        """

        return self._tokens[self._current - 1]

    def _is_at_end(self):
        """
        Returns whether the parser is at the end of the tokens list.

        :return: (boolean)
        """

        return self._peek().get_type() == TokenType.EOF

    def _synchronise(self):
        """
        Synchronises current pointer to a statement starting token. Used to prevent consecutive errors produced when
        one error occurs.

        :return: (None)
        """

        self._move()

        while not self._is_at_end():
            if self._peek().get_type() not in [
                TokenType.QUBIT,
                TokenType.NUMBER,
                TokenType.COMMA
            ]:
                return

            self._move()

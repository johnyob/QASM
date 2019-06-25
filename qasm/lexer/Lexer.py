import re as regular_expression

from qasm.lexer.TokenType import TokenType, KEYWORDS
from qasm.helpers.Constants import INTEGER_REGEX
from qasm.error.LexerError import LexerError
from qasm.lexer.Token import Token


class Lexer:

    def __init__(self, source):
        """
        Lexer constructor

        :param source: assembly source code (string)
        """

        self._source = source
        self._tokens = []
        self._errors = []

        self._start = 0
        self._current = 0
        self._line = 1

        if not self._source:
            self._error("File is empty", self._peek())

    def scan_tokens(self):
        """
        Performs lexical analysis on the source code to produce a list of tokens with a End Of File token at the
        end of the list.

        :return: (list)
        """

        while not self._is_at_end():
            self._start = self._current
            self._scan_token()

        self._tokens.append(Token(TokenType.EOF, "", None, self._line))
        return self._tokens

    def get_errors(self):
        """
        Fetches internal lexer errors

        :return: (list)
        """

        return self._errors

    def _case(self, character, comparable_character):
        """
        Helper method; used to mimic switch-case statement comparisons. e.g. java

        :param character: (string)
        :param comparable_character: (string)
        :return: (boolean)
        """

        return character == comparable_character

    def _scan_token(self):
        """
        Analyses the current character for a valid token. If a multi-character token is detected then a separate method
        is invoked to handle it. If an unexpected character is analysed then an error occurs.

        :return: (None)
        """

        character = self._move()
        if self._case(character, " "):
            pass
        elif self._case(character, "\r"):
            pass
        elif self._case(character, "\t"):
            pass
        elif self._case(character, ";"):
            while self._peek() != "\n" and not self._is_at_end():
                self._move()
        elif self._case(character, "\n"):
            self._line += 1
        elif self._case(character, ","):
            self._add_token(TokenType.COMMA)
        elif self._case(character, "q"):
            self._qubit()
        elif self._is_digit(character):
            self._number()
        elif self._is_alpha(character):
            self._instruction()
        else:
            self._error("Unexpected character", character)

    def _validate_integer(self, literal_string):
        """
        Method used to validate integer

        :param literal_string: (string)
        :return: (boolean)
        """

        if not regular_expression.match(INTEGER_REGEX, literal_string):
            self._error("Invalid integer format", self._peek())
            return False

        return True

    def _qubit(self):
        """
        Method used to handle the creation of a qubit token.
        Literal contains integer index of the qubit.
        Lexeme contains string representation of qubit reference e.g. q1, q2, qn, where 1 <= n <= x

        :return: (None)
        """

        while not self._is_at_end() and self._is_digit(self._peek()):
            self._move()

        literal_string = self._source[self._start + 1 : self._current]
        if not self._validate_integer(literal_string):
            return

        self._add_token_literal(TokenType.QUBIT, int(literal_string))

    def _number(self):
        """
        Method used to handle the creation of a number token.
        Literal contains float of the number.
        Lexeme contains string reference of number e.g. 10, 4.3

        :return: (None)
        """

        while not self._is_at_end() and self._is_digit(self._peek()):
            self._move()

        if self._peek() == "." and self._is_digit(self._peek_next()):
            self._move()
            while self._is_digit(self._peek()):
                self._move()

        literal = float(self._source[self._start : self._current])
        self._add_token_literal(TokenType.NUMBER, literal)

    def _instruction(self):
        """
        Method used to handle the creation of an instruction.
        Literal contains string representation of the instruction

        :return: (None)
        """

        while not self._is_at_end() and self._is_alpha_numeric(self._peek()):
            self._move()

        literal = self._source[self._start: self._current]
        type = KEYWORDS.get(literal, None)
        if not type:
            self._error("Invalid instruction", literal)
            return

        self._add_token_literal(type, literal)

    def _add_token(self, type):
        """
        Method that partially applies the add_token_literal method

        :param type: token type (qasm.lexer.TokenType.TokenType)
        :return: (None)
        """

        self._add_token_literal(type, None)

    def _add_token_literal(self, type, literal):
        """
        Method that appends a token to the tokens list.
        Parses lexeme from source using start and current pointers.

        :param type: token type (qasm.lexer.TokenType.TokenType)
        :param literal: literal of the token
        :return: (None)
        """

        lexeme = self._source[self._start : self._current]
        self._tokens.append(Token(type, lexeme, literal, self._line))

    def _is_digit(self, character):
        """
        Checks whether :param character is a digit

        :param character: (string)
        :return: (boolean)
        """

        return character.isdigit()

    def _is_alpha(self, character):
        """
        Checks whether :param character is an alphabet character

        :param character: (string)
        :return: (boolean)
        """

        return character.isalpha()

    def _is_alpha_numeric(self, character):
        """
        Checks whether :param character is an alpha numerical character

        :param character: (string)
        :return: (boolean)
        """

        return self._is_digit(character) or self._is_alpha(character)

    def _move(self):
        """
        Increments the current pointer and returns the previous character

        :return: (string)
        """

        self._current += 1
        return self._source[self._current - 1]

    def _peek(self):
        """
        Returns the current character

        :return: (string)
        """

        if self._is_at_end():
            return '\0'

        return self._source[self._current]

    def _peek_next(self):
        """
        Returns the next character

        :return: (string)
        """

        if self._current + 1 >= len(self._source):
            return '\0'

        return self._source[self._current + 1]

    def _is_at_end(self):
        """
        Returns whether the lexer is at the end of the source code

        :return: (boolean)
        """

        return self._current >= len(self._source)

    def _error(self, message, character):
        """
        Constructs a lexer error and appends it to the internal errors list

        :param message: error message (string)
        :param character: character that raised the error (string)
        :return: (None)
        """

        self._errors.append(LexerError(self._line, message, character))

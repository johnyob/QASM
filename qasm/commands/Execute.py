import sys

from qasm.commands.Command import Command
from qasm.helpers.Util import read_file
from qasm.parser.Parser import Parser
from qasm.lexer.Lexer import Lexer
from qasm.bridge.Bridge import Bridge
from qasm.bridge.config.QuantumComputerConfig import QuantumComputerConfig


class Execute(Command):

    def __init__(self, arguments):
        super().__init__(arguments)
        self._file_location = self._arguments["<file>"]

    def run(self):
        errors, bridge_errors = self._run(read_file(self._file_location))

        if errors:
            sys.exit(65)

        if bridge_errors:
            sys.exit(70)

    def _run(self, source):

        lexer_errors, parser_errors, bridge_errors = [], [], []

        lexer = Lexer(source)
        tokens = lexer.scan_tokens()

        lexer_errors = lexer.get_errors()
        self._print_errors(lexer_errors)
        if lexer_errors:
            return lexer_errors + parser_errors, bridge_errors

        parser = Parser(tokens)
        statements = parser.parse()

        parser_errors = parser.get_errors()
        self._print_errors(parser_errors)

        if parser_errors:
            return lexer_errors + parser_errors, bridge_errors

        bridge = Bridge(
            statements, QuantumComputerConfig.get_qubits()
        )

        bridge.execute()
        bridge_errors = bridge.get_errors()

        self._print_errors(bridge_errors)
        return lexer_errors + parser_errors, bridge_errors

    def _print_errors(self, errors):
        for error in errors:
            if hasattr(error, "report"):
                print(error.report(), file=sys.stderr)
            else:
                print("[ERROR] Error: QASMPythonError, Response: {0}".format(error), file=sys.stderr)

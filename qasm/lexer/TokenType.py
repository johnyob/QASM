from enum import Enum as Enumerate

import qasm.parser.Statement as Statement


class TokenType(Enumerate):
    QUBIT = 1
    NUMBER = 2
    COMMA = 3
    EOF = 4

    X = 5
    Y = 6
    Z = 7
    H = 8
    R = 9
    SQRT_NOT = 10
    MEASURE = 11


KEYWORDS = {
    "X": TokenType.X,
    "Y": TokenType.Y,
    "Z": TokenType.Z,
    "H": TokenType.H,
    "R": TokenType.R,
    "SqrtNOT": TokenType.SQRT_NOT,
    "MEASURE": TokenType.MEASURE
}

STATEMENTS = {
    5: Statement.PauliX,
    6: Statement.PauliY,
    7: Statement.PauliZ,
    8: Statement.Hadamard,
    9: Statement.PhaseShift,
    10: Statement.SqrtNot,
    11: Statement.Measure
}

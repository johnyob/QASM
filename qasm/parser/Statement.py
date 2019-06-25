from abc import ABC as Abstract, abstractmethod


class StatementVisitor(Abstract):
    """
    Abstract class.
    Used to traverse the abstract syntax tree produced by the parser.
    """

    @abstractmethod
    def visit_pauli_x_statement(self, statement):
        pass

    @abstractmethod
    def visit_pauli_y_statement(self, statement):
        pass

    @abstractmethod
    def visit_pauli_z_statement(self, statement):
        pass

    @abstractmethod
    def visit_hadamard_statement(self, statement):
        pass

    @abstractmethod
    def visit_phase_shift_statement(self, statement):
        pass

    @abstractmethod
    def visit_sqrt_not_statement(self, statement):
        pass

    @abstractmethod
    def visit_measure_statement(self, statement):
        pass


class Statement(Abstract):
    """
    Parent class of the Statement class.
    Inherited by all statement objects.
    """

    @abstractmethod
    def accept(self, visitor):
        pass


class PauliX(Statement):

    def __init__(self, qubit):
        """
        Pauli X gate application statement constructor

        :param qubit: qubit that the pauli x gate will be applied too (token)
        """

        self._qubit, = qubit

    def get_qubit(self):
        """
        Returns qubit operand

        :return: (qasm.lexer.Token.Token)
        """

        return self._qubit

    def accept(self, visitor):
        """
        Traversal method.
        Used to process of the node of abstract syntax tree.

        :param visitor: visitor class (sub-class of the StatementVisitor class)
        :return:
        """

        return visitor.visit_pauli_x_statement(self)

    def __repr__(self):
        """
        Returns string representation of pauli x gate application statement

        :return: (string)
        """

        return "X {0}".format(self._qubit)


class PauliY(Statement):

    def __init__(self, qubit):
        """
        Pauli Y gate application statement constructor

        :param qubit: qubit that the pauli y gate will be applied too (token)
        """

        self._qubit, = qubit

    def get_qubit(self):
        """
        Returns qubit operand

        :return: (qasm.lexer.Token.Token)
        """

        return self._qubit

    def accept(self, visitor):
        """
        Traversal method.
        Used to process of the node of abstract syntax tree.

        :param visitor: visitor class (sub-class of the StatementVisitor class)
        :return:
        """

        return visitor.visit_pauli_y_statement(self)

    def __repr__(self):
        """
        Returns string representation of pauli y gate application statement

        :return: (string)
        """

        return "Y {0}".format(self._qubit)


class PauliZ(Statement):

    def __init__(self, qubit):
        """
        Pauli Z gate application statement constructor

        :param qubit: qubit that the pauli z gate will be applied too (token)
        """

        self._qubit, = qubit

    def get_qubit(self):
        """
        Returns qubit operand

        :return: (qasm.lexer.Token.Token)
        """

        return self._qubit

    def accept(self, visitor):
        """
        Traversal method.
        Used to process of the node of abstract syntax tree.

        :param visitor: visitor class (sub-class of the StatementVisitor class)
        :return:
        """

        return visitor.visit_pauli_z_statement(self)

    def __repr__(self):
        """
        Returns string representation of pauli z gate application statement

        :return: (string)
        """

        return "Z {0}".format(self._qubit)


class Hadamard(Statement):

    def __init__(self, qubit):
        """
        Hadamard gate application statement constructor

        :param qubit: qubit that the hadamard gate will be applied too (token)
        """

        self._qubit, = qubit

    def get_qubit(self):
        """
        Returns qubit operand

        :return: (qasm.lexer.Token.Token)
        """

        return self._qubit

    def accept(self, visitor):
        """
        Traversal method.
        Used to process of the node of abstract syntax tree.

        :param visitor: visitor class (sub-class of the StatementVisitor class)
        :return:
        """

        return visitor.visit_hadamard_statement(self)

    def __repr__(self):
        """
        Returns string representation of hadamard gate application statement

        :return: (string)
        """
        print(type(self._qubit))
        return "H {0}".format(self._qubit)


class PhaseShift(Statement):

    def __init__(self, tokens):
        """
        Phase shift gate application statement constructor

        :param tokens: (|tokens|=2) (list)
        """

        self._phi, self._qubit = tokens

    def get_qubit(self):
        """
        Returns qubit operand

        :return: (qasm.lexer.Token.Token)
        """

        return self._qubit

    def get_phi(self):
        """
        Returns phi operand

        :return: (qasm.lexer.Token.Token)
        """

        return self._phi

    def accept(self, visitor):
        """
        Traversal method.
        Used to process of the node of abstract syntax tree.

        :param visitor: visitor class (sub-class of the StatementVisitor class)
        :return:
        """

        return visitor.visit_phase_shift_statement(self)

    def __repr__(self):
        """
        Returns string representation of phase shift gate application statement

        :return: (string)
        """
        #print(type(self._qubit))

        return "R {0}, {1}".format(self._phi, self._qubit)


class SqrtNot(Statement):

    def __init__(self, qubit):
        """
        Sqrt Not gate application statement constructor

        :param qubit: qubit that the Sqrt Note gate will be applied too (token)
        """

        self._qubit, = qubit

    def get_qubit(self):
        """
        Returns qubit operand

        :return: (qasm.lexer.Token.Token)
        """

        return self._qubit

    def accept(self, visitor):
        """
        Traversal method.
        Used to process of the node of abstract syntax tree.

        :param visitor: visitor class (sub-class of the StatementVisitor class)
        :return:
        """

        return visitor.visit_sqrt_not_statement(self)

    def __repr__(self):
        """
        Returns string representation of Sqrt Not gate application statement

        :return: (string)
        """

        return "SqrtNOT {0}".format(self._qubit)


class Measure(Statement):

    def __init__(self, tokens):
        """
        Measure statement constructor
        """

        pass

    def accept(self, visitor):
        """
        Traversal method.
        Used to process of the node of abstract syntax tree.

        :param visitor: visitor class (sub-class of the StatementVisitor class)
        :return:
        """

        return visitor.visit_measure_statement(self)

    def __repr__(self):
        """
        Returns string representation of measure statement

        :return: (string)
        """

        return "MEASURE"

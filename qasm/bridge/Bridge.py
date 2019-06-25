from qasm.parser.Statement import StatementVisitor
from qasm.error.BridgeError import BridgeError
from quantum_computer import Computer


class Bridge(StatementVisitor):

    def __init__(self, statements, qubits):
        """
        Bridge constructor.
        Bridge for qasm.parser.Statement.Statement objects.
        Constructs a interface between the ASM and the Quantum Computer

        :param statements: list of statements produced by the parser (list)
        :param registers: number of qubits in quantum computer (integer)
        """

        self._statements = statements

        self._qubits = qubits
        self._quantum_computer = Computer(qubits)

        self._errors = []

    def _validate_qubit(self, qubit):
        """
        If :param qubit out of index range -> bridge error raised.

        :param qubit: (qasm.lexer.Token.Token)
        :return: (None)
        """

        if not 1 <= qubit.get_literal() <= self._qubits:
            raise BridgeError(qubit, "Qubit index out of range")

    def visit_pauli_x_statement(self, statement):
        """
        Handles pauli x gate application to the quantum register stored in _quantum_computer

        :param statement: (qasm.parser.Statement.PauliX)
        :return: (None)
        """

        qubit = statement.get_qubit()
        self._validate_qubit(qubit)

        self._quantum_computer.X(qubit.get_literal())

    def visit_pauli_y_statement(self, statement):
        """
        Handles pauli y gate application to the quantum register stored in _quantum_computer

        :param statement: (qasm.parser.Statement.PauliY)
        :return: (None)
        """

        qubit = statement.get_qubit()
        self._validate_qubit(qubit)

        self._quantum_computer.Y(qubit.get_literal())

    def visit_pauli_z_statement(self, statement):
        """
        Handles pauli z gate application to the quantum register stored in _quantum_computer

        :param statement: (qasm.parser.Statement.PauliZ)
        :return: (None)
        """

        qubit = statement.get_qubit()
        self._validate_qubit(qubit)

        self._quantum_computer.Z(qubit.get_literal())

    def visit_hadamard_statement(self, statement):
        """
        Handles hadamard gate application to the quantum register stored in _quantum_computer

        :param statement: (qasm.parser.Statement.Hadamard)
        :return: (None)
        """

        qubit = statement.get_qubit()
        self._validate_qubit(qubit)

        self._quantum_computer.H(qubit.get_literal())

    def visit_phase_shift_statement(self, statement):
        """
        Handles phase shift gate application to the quantum register stored in _quantum_computer

        :param statement: (qasm.parser.Statement.PhaseShift)
        :return: (None)
        """

        qubit = statement.get_qubit()
        self._validate_qubit(qubit)

        self._quantum_computer.R(qubit.get_literal(), statement.get_phi().get_literal())

    def visit_sqrt_not_statement(self, statement):
        """
        Handles sqrt not gate application to the quantum register stored in _quantum_computer

        :param statement: (qasm.parser.Statement.SqrtNot)
        :return: (None)
        """

        qubit = statement.get_qubit()
        self._validate_qubit(qubit)

        self._quantum_computer.SqrtNOT(qubit.get_literal())

    def visit_measure_statement(self, statement):
        """
        Handles quantum register stored in _quantum_computer observation algorithm

        :param statement: (qasm.parser.Statement.Measure)
        :return: (None)
        """

        print(self._quantum_computer.measure())

    def execute(self):
        """
        Executes statements stored in _statements.
        If a bridge (or error from the quantum computer) error occurs during the execution of statements, then the
        error is appended to the internal errors list and the program is halted.

        :return: (None)
        """

        try:
            for statement in self._statements:
                self._execute_statement(statement)
        except (BridgeError, Exception) as error:
            self._error(error)
            return

    def _execute_statement(self, statement):
        """
        Executes :param statement using public AST (Abstract Syntax Tree) traversal method.

        :param statement: (qasm.parser.Statement.Statement)
        :return: (None)
        """

        statement.accept(self)

    def _error(self, error):
        """
        Appends bridge error :param error to internal errors list

        :param error: (qasm.error.VirtualMachineError)
        :return: (None)
        """

        self._errors.append(error)

    def get_errors(self):
        """
        Returns internal bridge errors

        :return: (list)
        """

        return self._errors

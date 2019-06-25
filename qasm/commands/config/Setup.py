import re as regular_expression
import json
import sys

from ascii_table import Table

from qasm.helpers.Constants import QUBITS_REGEX, QC_CONFIG
from qasm.helpers.Exceptions import QASMConfigException
from qasm.helpers.Util import write_file, SortedDictionary
from qasm.commands.Command import Command


class Setup(Command):

    def run(self):
        """
        Run method for config setup

        :return: (None)
        """

        qubits = input("Enter number of qubits in the quantum computer: ")

        if not regular_expression.match(QUBITS_REGEX, qubits):
            print(QASMConfigException({
                "message": "invalid number of qubits",
                "format": "[0-9]{1,2}",
                "qubits": qubits
            }), file=sys.stderr)
            return

        config = {
            "qubits": int(qubits)
        }
        write_file(QC_CONFIG, json.dumps(config))

        config = SortedDictionary(config)
        print("\nQuantum Computer Config")
        print(Table([config.names(), config.values()]))

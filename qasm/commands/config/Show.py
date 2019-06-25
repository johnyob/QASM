from ascii_table import Table

from qasm.bridge.config.QuantumComputerConfig import QuantumComputerConfig
from qasm.helpers.Util import SortedDictionary
from qasm.commands.Command import Command


class Show(Command):

    def run(self):
        """
        Return method for config show command

        :return: (None)
        """

        config = SortedDictionary(QuantumComputerConfig.get_config())

        print("\nQuantum Computer Config")
        print(Table([config.names(), config.values()]))

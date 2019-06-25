"""
Quantum Assembly (QASM)

Usage:
  qasm config setup
  qasm config show
  qasm execute <file>

Options:
  -h --help                 Show this screen.
  --version                 Show version.
"""

from importlib import import_module
from functools import reduce
from docopt import docopt
import json

from qasm.helpers.Constants import COMMANDS_JSON
from qasm.helpers.Util import read_file
from qasm import __version__

class Client:

    def __init__(self):
        """
        Client Class.
        Retrieves options from docopt. Options are then filtered using data stored in commands.json.
        Command is then imported and instantiated.
        """

        self._options = docopt(__doc__, version=__version__)
        self._arguments = {
            k: v for k, v in self._options.items()
            if not isinstance(v, bool)
        }

        commands_json = json.loads(read_file(COMMANDS_JSON))
        command = list(filter(lambda x: self._is_command(x["Conditions"]), commands_json))[0]

        getattr(
            import_module("qasm.commands.{0}".format(command["Module Identifier"])),
            command["Class Identifier"]
        )(self._arguments).run()

    def _is_command(self, conditions):
        return reduce(lambda x, y: x and y, map(lambda y: self._options[y], conditions))
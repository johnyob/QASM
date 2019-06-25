import os

from qasm import ROOT, OS

separator = "\\" if OS == "nt" else "/"

SYNTAX_JSON = os.path.join(ROOT, "parser{0}syntax.json".format(separator))
COMMANDS_JSON = os.path.join(ROOT, "commands.json")
QC_CONFIG = os.path.join(ROOT, "bridge{0}config{0}config.json".format(separator))


INTEGER_REGEX = r"^(\d+)$"
QUBITS_REGEX = r"^(\d{1,2})$"
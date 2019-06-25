import json

from qasm.helpers.Exceptions import QASMConfigException
from qasm.helpers.Constants import QC_CONFIG
from qasm.helpers.Util import read_file


class QuantumComputerConfig:

    @staticmethod
    def get_config():
        try:
            return json.loads(read_file(QC_CONFIG))
        except:
            raise QASMConfigException({
                "message": "quantum computer config not setup. Please use qasm config setup."
            })

    @staticmethod
    def get_qubits():
        return QuantumComputerConfig.get_config()["qubits"]


import setuptools

requires = [
    "docopt",
    "ascii-table>=0.0.2",
    "numpy"
]

packages = [
    "qasm",
    "qasm.bridge",
    "qasm.bridge.config",
    "qasm.parser",
    "qasm.lexer",
    "qasm.helpers",
    "qasm.error",
    "qasm.commands",
    "qasm.commands.config",
    "quantum_computer",
    "quantum_computer.gates",
    "quantum_computer.helpers",
    "quantum_computer.simulator"
]

setuptools.setup(
    name="qasm",
    version="0.0.1",
    author="Anonymous",
    description="QASM NEA.",
    include_package_data=True,
    packages=packages,
    install_requires=requires,
    entry_points={
        "console_scripts": [
            "qasm=qasm.__main__:main"
        ]
    }
)
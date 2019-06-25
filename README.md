# QASM
> A *very* simple quantum assembler

This is a very simple proof of concept Python package for a simple quantum assembler.

## Features

- [x] Custom quantum register configuration
- [x] Quantum measurement
- [x] Pauli-X gate
- [x] Pauli-Y gate
- [x] Hadamard gate
- [x] Phase shift gate
- [x] Square root of NOT gate

## Installation
```sh
python -m pip install --no-cache-dir --index-url <pypi package upload TODO>
```

## Usage
### Help

```sh
C:\>qasm -help
Quantum Assembly (QASM)

Usage:
  qasm config setup
  qasm config show
  qasm execute <file>

Options:
  -h --help                 Show this screen.
  --version                 Show version.

Help:
  For help using this client, please see https://github.com/johnyob/QASM
```

### Config Setup

To setup the config of the quantum register, the command ``qasm config setup`` must be used. Note that if the config for the register has not been setup / selected then a ``QASMConfigException`` is raised.
```sh
C:\>qasm config setup
Enter number of qubits in the quantum computer: 10

Quantum Computer Config
 +--------+-------+
 |  Name  | Value |
 +--------+-------+
 | qubits | 10    |
 +--------+-------+
```

### Config Show

The configuration for the register can be displayed in an ascii-table using ``qasm config show``.

```sh
C:\>qasm config show

Quantum Computer Config
 +--------+-------+
 |  Name  | Value |
 +--------+-------+
 | qubits | 10    |
 +--------+-------+
```

### Syntax

The syntax for the implementation of QASM can be described using the following grammar:
```sh
<program> ::= <statement> <program> | <statement>;
<statement> ::= X <qubit>
              | Y <qubit>
              | Z <qubit>
              | H <qubit>
              | R <number>, <qubit>
              | SqrtNOT <qubit>
              | MEASURE;
<qubit> ::= q<integer>;
<integer> ::= <digit> <integer> | <digit>;
<number> ::= <integer> | <integer>.<integer>;
<digit> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9;
```

### Example

To execute a QASM program, we use the command ``qasm execute <file name>``. For example, suppose we have the quantum program that models an 8-sides quantum dice that generates a random result. First we must change the configuration of the register to only contain three qubits (as 2^3 = 8 possibilities).
```sh
C:\>qasm config setup
Enter number of qubits in the quantum computer: 3

Quantum Computer Config
 +--------+-------+
 |  Name  | Value |
 +--------+-------+
 | qubits | 3     |
 +--------+-------+
```

So the register is now setup to execute the following program saved as ``quantum_dice.qasm``:
```
H q1
H q2
H q3
MEASURE
```

Using the afformentioned command produces the output:
```sh
C:\>qasm execute quantum_dice.qasm
|psi> = |000>

C:\>qasm execute quantum_dice.qasm
|psi> = |010>

C:\>qasm execute quantum_dice.qasm
|psi> = |100>
```

## Errors
If you discover an error within this package, please email [me](mailto:alistair@duneroot.co.uk).

## Credits
- [Alistair O'Brien](https://github.com/johnyob)

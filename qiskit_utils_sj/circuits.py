from qiskit import QuantumCircuit

def simple_bell_pair() -> QuantumCircuit:
    """Create a simple 2-qubit Bell pair circuit."""
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])
    return qc

def ghz_state(n: int) -> QuantumCircuit:
    """Create an n-qubit GHZ state circuit."""
    qc = QuantumCircuit(n, n)
    qc.h(0)
    for i in range(n-1):
        qc.cx(i, i+1)
    qc.measure(range(n), range(n))
    return qc


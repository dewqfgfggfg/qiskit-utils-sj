from qiskit import Aer, execute
from qiskit.visualization import plot_histogram

def quick_simulate(qc, shots=1024, draw=True):
    """Run a quick simulation on qasm_simulator."""
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend=backend, shots=shots)
    result = job.result()
    counts = result.get_counts()
    if draw:
        plot_histogram(counts).show()
    return counts


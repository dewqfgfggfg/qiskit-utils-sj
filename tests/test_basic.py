from qiskit_utils_sj import circuits

def test_bell_pair():
    qc = circuits.simple_bell_pair()
    assert qc.num_qubits == 2
    assert qc.num_clbits == 2


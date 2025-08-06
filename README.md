# qiskit-utils-sj

Qiskit beginners-friendly utility package created by **Sunjun Hwang**  
Easily generate quantum circuits, visualize Bloch spheres, and run quick simulations.

---

## Features

- **Circuit Generator**: Quickly create Bell pairs or GHZ states.
- **Quick Simulator**: Run `qasm_simulator` and get histogram results with one function.
- **Visualization Tools**: Plot Bloch sphere vectors for single-qubit states.

---

## Installation

Clone the repository and install in editable mode:

```bash
git clone https://github.com/yourname/qiskit-utils-sj.git
cd qiskit-utils-sj
pip install -e .
```


---

## Example Usage

```python
from qiskit_utils_sj import circuits, simulators

qc = circuits.simple_bell_pair()
qc.draw('mpl')

result = simulators.quick_simulate(qc, shots=1024)
print(result)
```
Check the `examples/basic_demo.py` notebook for more details.

---


## License
This project is licensed under the MIT License - see the LICENSE file for details.


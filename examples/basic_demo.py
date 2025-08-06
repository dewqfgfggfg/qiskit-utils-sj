# basic_demo.ipynb

# 1. 패키지 임포트
from qiskit_utils_sj import circuits, simulators, visualization

# 2. 간단한 Bell Pair 회로 생성
qc = circuits.simple_bell_pair()
qc.draw('mpl')

# 3. 시뮬레이션 실행
result = simulators.quick_simulate(qc, shots=1024)
print("Simulation result:", result)

# 4. Bloch Sphere 시각화 예제
# |+> 상태를 Bloch 벡터 (x=1, y=0, z=0)로 표현
visualization.plot_bloch_vector([1,0,0])


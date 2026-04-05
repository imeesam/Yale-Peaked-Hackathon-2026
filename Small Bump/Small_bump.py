from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# 1. Load the specific problem file
circuit = QuantumCircuit.from_qasm_file('P2_small_bump.qasm')

# 2. Add measurements to all qubits
circuit.measure_all()

# 3. Set up the local simulator
simulator = AerSimulator()

# 4. Run the circuit locally (10,000 shots)
job = simulator.run(circuit, shots=10000)
result = job.result()
counts = result.get_counts(circuit)

# 5. Find the Peak Bitstring
sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)

print("Top 3 most probable bitstrings:")
for bitstring, count in sorted_counts[:3]:
    print(f"Bitstring: {bitstring} | Count: {count}")

print(f"\n🚀 The hidden peak bitstring is: {sorted_counts[0][0]}")
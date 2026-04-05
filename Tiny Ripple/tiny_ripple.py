from qiskit import QuantumCircuit
import bluequbit

# 1. Initialize BlueQubit with your token
# Replace "YOUR_API_TOKEN" with the actual token you copied from their website
bq = bluequbit.init("PsahvWtgOrZdb0EvkCLcCmaphu4sJpOw")

# 2. Load the specific problem file
circuit = QuantumCircuit.from_qasm_file('P3_tiny_ripple.qasm') # update if the filename is different

# Add measurements to all qubits
circuit.measure_all()

# 3. Run on BlueQubit's Cloud 
# This sends the circuit to their servers, uses your credits, and returns the result
print("🚀 Submitting job to BlueQubit cloud... This might take a moment.")
job = bq.run(circuit, shots=10000) 
result = job.get_counts()

# 4. Find the Peak Bitstring
sorted_counts = sorted(result.items(), key=lambda item: item[1], reverse=True)

print("\nTop 3 most probable bitstrings:")
for bitstring, count in sorted_counts[:3]:
    print(f"Bitstring: {bitstring} | Count: {count}")

print(f"\n🎉 The hidden peak bitstring is: {sorted_counts[0][0]}")
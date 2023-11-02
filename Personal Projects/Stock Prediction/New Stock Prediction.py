import qiskit as qt
import numpy as np

qc = qt.QuantumCircuit()
qr = qt.QuantumRegister(3,"q")
qc.add_register(qr)

qc.rx(np.pi/2, qr[1])
qc.cz(qr[2],qr[1])
qc.rx(-np.pi/2, qr[1])

qc.rx(np.pi/4, qr[2])
qc.cz(qr[1],qr[2])
qc.rx(-np.pi/4, qr[2])
qc.cz(qr[1],qr[2])
qc.cz(qr[0],qr[2])
qc.rx(-np.pi/4, qr[2])
qc.cz(qr[1],qr[2])
qc.rx(np.pi/4, qr[2])

qc.rx(-np.pi/2, qr[1])
qc.cz(qr[2],qr[1])
qc.rx(np.pi/2, qr[1])

qc.measure_all()

qc.draw()
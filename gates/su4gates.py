from qiskit import QuantumCircuit
import random
import math


def random_angle():
    return random.uniform(0, 1) * 2 * math.pi


def su_4():
    qc = QuantumCircuit(2)
    qc.u(random_angle(), random_angle(), random_angle(), 0)
    qc.u(random_angle(), random_angle(), random_angle(), 1)
    qc.cx(0, 1)
    qc.u(random_angle(), random_angle(), random_angle(), 0)
    qc.u(random_angle(), random_angle(), random_angle(), 1)
    qc.cx(1, 0)
    qc.u(random_angle(), random_angle(), random_angle(), 0)
    qc.cx(0, 1)
    qc.u(random_angle(), random_angle(), random_angle(), 0)
    qc.u(random_angle(), random_angle(), random_angle(), 1)
    return qc


def su_4_with_values(theta: float = 0, phi: float = 0, lam: float = 0):
    qc = QuantumCircuit(2)
    qc.u(theta, phi, lam, 0)
    qc.u(theta, phi, lam, 1)
    qc.cx(0, 1)
    qc.u(theta, phi, lam, 0)
    qc.u(theta, phi, lam, 1)
    qc.cx(1, 0)
    qc.u(theta, phi, lam, 0)
    qc.cx(0, 1)
    qc.u(theta, phi, lam, 0)
    qc.u(theta, phi, lam, 1)
    return qc

import sys
sys.path.append("../")
import numpy as np
from rdybergrmt import *
L = 2
V = -1
h = 0
H = Spin_interaction_hamiltonian(L, V = V, hopping_type = "1D_NN_PBC", coefficient_type = "Constant").get_Hamiltonian_Szz() + Spin_field_hamiltonian(L, h, coefficient_type = "Constant").get_Hamiltonian_Sx()
print(H)
evalue , evector = np.linalg.eigh(H)
Ground_energy = evalue[0]
Ground_vector = evector[:,0]
print(Ground_energy)
print(Ground_vector)
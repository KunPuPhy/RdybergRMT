import sys
sys.path.append("../")
import unittest
import numpy as np
from scipy import sparse
from rdybergrmt import *


class TestSpinFieldHamiltonian(unittest.TestCase):
    def test_get_hamiltonian_Sx_L1(self):
        L = 1
        h = 1
        H = Spin_field_hamiltonian(L, h, coefficient_type="Constant").get_hamiltonian_Sx()
        expected_H = np.array([[0, 1], [1, 0]])
        self.assertTrue(np.array_equal(H, expected_H))

    def test_get_Hamiltonian_Sz_L1(self):
        L = 1
        h = 1
        H = Spin_field_hamiltonian(L, h, coefficient_type="Constant").get_Hamiltonian_Sz()
        expected_H = np.array([[-1, 0], [0, 1]])
        self.assertTrue(np.array_equal(H, expected_H))

    def test_get_Hamiltonian_Sy_L1(self):
        L = 1
        h = 1
        H = Spin_field_hamiltonian(L, h, coefficient_type="Constant").get_Hamiltonian_Sy()
        expected_H = np.array([[0, 0 + 1j], [0 - 1j, 0]])
        self.assertTrue(np.array_equal(H, expected_H))


class TestSpinInteractionHamiltonian(unittest.TestCase):
    def test_get_Hamiltonian_Sxx_L2(self):
        L = 2
        V = 1
        H = Spin_interaction_hamiltonian(L, V, coefficient_type="Constant", hopping_type="1D_NN_OBC").get_Hamiltonian_Sxx()
        expected_H = np.array([[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]])
        self.assertTrue(np.array_equal(H, expected_H))

    def test_get_Hamiltonian_Szz_L2(self):
        L = 2
        V = 1
        H = Spin_interaction_hamiltonian(L, V, coefficient_type="Constant", hopping_type="1D_NN_OBC").get_Hamiltonian_Szz()
        expected_H = np.array([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
        self.assertTrue(np.array_equal(H, expected_H))

    def test_get_Hamiltonian_Syy_L2(self):
        L = 2
        V = 1
        H = Spin_interaction_hamiltonian(L, V, coefficient_type="Constant", hopping_type="1D_NN_OBC").get_Hamiltonian_Syy()
        expected_H = np.array([[0, 0, 0, -1], [0, 0, 1, 0], [0, 1, 0, 0], [-1, 0, 0, 0]])
        self.assertTrue(np.array_equal(H, expected_H))

if __name__ == '__main__':
    unittest.main()
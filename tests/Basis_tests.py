import sys
sys.path.append("../")
import unittest
from rdybergrmt import *


class TestGetSpinBasis(unittest.TestCase):
    def test_get_spin_basis_L_0(self):
        self.assertEqual(get_spin_basis(0), [0])

    def test_get_spin_basis_L_1(self):
        self.assertEqual(get_spin_basis(1), [0, 1])

    def test_get_spin_basis_L_2(self):
        self.assertEqual(get_spin_basis(2), [0, 1, 2, 3])

    def test_get_spin_basis_L_3(self):
        self.assertEqual(get_spin_basis(3), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_get_spin_basis_L_5(self):
        self.assertEqual(get_spin_basis(5), list(range(2**5)))


if __name__ == '__main__':
    unittest.main()
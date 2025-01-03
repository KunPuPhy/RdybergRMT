import sys
sys.path.append("../")
import unittest
from rdybergrmt import *


class TestSearchI(unittest.TestCase):
    """
    
    Tests for the search_i function.

    """
    def test_search_i_ElementAtStart(self):
        basis = [1, 2, 3, 4, 5]
        i = 1
        self.assertEqual(search_i(basis, i), 0)

    def test_search_i_ElementInMiddle(self):
        basis = [1, 2, 3, 4, 5]
        i = 3
        self.assertEqual(search_i(basis, i), 2)

    def test_search_i_ElementAtEnd(self):
        basis = [1, 2, 3, 4, 5]
        i = 5
        self.assertEqual(search_i(basis, i), 4)

    def test_search_i_ElementNotFound(self):
        basis = [1, 2, 3, 4, 5]
        i = 7
        self.assertEqual(search_i(basis, i), False)

    def test_search_i_ElementLessThanMin(self):
        basis = [1, 2, 3, 4, 5]
        i = 0
        self.assertEqual(search_i(basis, i), False)

    def test_search_i_ElementGreaterThanMax(self):
        basis = [1, 2, 3, 4, 5]
        i = 6
        self.assertEqual(search_i(basis, i), False)

    def test_search_i_ElementNotInList(self):
        basis = [1, 2, 4, 5]
        i = 3
        self.assertEqual(search_i(basis, i), False)

    def test_search_i_EmptyBasis(self):
        basis = []
        i = 1
        self.assertEqual(search_i(basis, i), False)

    def test_search_i_SingleElementMatch(self):
        basis = [1]
        i = 1
        self.assertEqual(search_i(basis, i), 0)

    def test_search_i_SingleElementNoMatch(self):
        basis = [1]
        i = 2
        self.assertEqual(search_i(basis, i), False)


class TestGetSpinBasis(unittest.TestCase):
    """
    
    Tests for the get_spin_basis function.
    
    """
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
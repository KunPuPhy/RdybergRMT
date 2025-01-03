import sys
sys.path.append("../")
import unittest
from rdybergrmt import *
#=====================================================================================================

class TestOneDimensionChainHoppingList(unittest.TestCase):
    def test_get_hopping_list_N_OBC(self):
        # Test case for minimum length
        L = 2
        hopping_list = OneDimension_chain_hopping_list(L).get_hopping_list_NN_OBC()
        self.assertEqual(hopping_list, [[0, 1]])

        # Test case for typical length
        L = 4
        hopping_list = OneDimension_chain_hopping_list(L).get_hopping_list_NN_OBC()
        self.assertEqual(hopping_list, [[0, 1], [1, 2], [2, 3]])

    def test_get_hopping_list_NN_OBC(self):
        # Test case for minimum length
        L = 3
        hopping_list = OneDimension_chain_hopping_list(L).get_hopping_list_NNN_OBC()
        self.assertEqual(hopping_list, [[0, 2]])

        # Test case for typical length
        L = 4
        hopping_list = OneDimension_chain_hopping_list(L).get_hopping_list_NNN_OBC()
        self.assertEqual(hopping_list, [[0, 2], [1, 3]])

    def test_get_hopping_list_N_PBC(self):
        # Test case for minimum length
        L = 2
        hopping_list = OneDimension_chain_hopping_list(L).get_hopping_list_NN_PBC()
        self.assertEqual(hopping_list, [[0, 1], [1, 0]])

        # Test case for typical length
        L = 4
        hopping_list = OneDimension_chain_hopping_list(L).get_hopping_list_NN_PBC()
        self.assertEqual(hopping_list, [[0, 1], [1, 2], [2, 3], [3, 0]])

    def test_get_hopping_list_NN_PBC(self):
        # Test case for minimum length
        L = 5
        hopping_list = OneDimension_chain_hopping_list(L).get_hopping_list_NNN_PBC()
        self.assertEqual(hopping_list, [[0, 2], [1, 3], [2, 4], [3, 0], [4, 1]])

        # Test case for typical length
        L = 5
        hopping_list = OneDimension_chain_hopping_list(L).get_hopping_list_NNN_PBC()
        self.assertEqual(hopping_list, [[0, 2], [1, 3], [2, 4], [3, 0], [4, 1]])


#======================================================================================================
if __name__ == '__main__':
    unittest.main()
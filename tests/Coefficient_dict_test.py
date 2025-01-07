import unittest
import sys
sys.path.append("../")
import numpy as np
from rdybergrmt import *


class TestFieldCoefficientDict(unittest.TestCase):
    '''
    
    Tests for Field_coefficient_dict

    '''
    def setUp(self):
        self.L = 3
        self.h = 1
        self.alpha = (np.sqrt(5) - 1) / 2
        self.delta = 0
        self.field_coefficient = Field_coefficient_dict(self.L, self.h, self.alpha, self.delta)

    def test_get_constant_coefficient(self):
        expected = {0: self.h, 1: self.h, 2: self.h}
        self.assertEqual(self.field_coefficient.get_constant_coefficient(), expected)

    def test_get_quasiperiodic_coefficient(self):
        expected = {i: self.h * np.cos(2 * np.pi * self.alpha * i + self.delta) for i in range(self.L)}
        self.assertEqual(self.field_coefficient.get_quasiperiodic_coefficient(), expected)

    def test_get_constant_vs_quasiperiodic_coefficient(self):
        expected = {i: self.h + self.h * np.cos(2 * np.pi * self.alpha * i + self.delta) for i in range(self.L)}
        self.assertEqual(self.field_coefficient.get_constant_vs_quasiperiodic_coefficient(), expected)


class TestInteractionCoefficientDict(unittest.TestCase):
    '''
    
    Tests for Interaction_coefficient_dict
    
    '''
    def setUp(self):
        self.L = 3
        self.V = 1
        self.alpha = (np.sqrt(5) - 1) / 2
        self.delta = 0
        self.hopping_type = "1D_NN_OBC"
        self.interaction_coefficient = Interaction_coefficient_dict(self.L, self.V, self.alpha, self.delta, self.hopping_type)

    def test_get_constant_coefficient(self):
        expected = {i: self.V for i in range(len(self.interaction_coefficient.hopping_list))}
        self.assertEqual(self.interaction_coefficient.get_constant_coefficient(), expected)

    def test_get_quasiperiodic_coefficient(self):
        expected = {i: self.V * np.cos(2 * np.pi * self.alpha * pos_i + self.delta) for i, (pos_i, _) in enumerate(self.interaction_coefficient.hopping_list)}
        self.assertEqual(self.interaction_coefficient.get_quasiperiodic_coefficient(), expected)

    def test_get_constant_vs_quasiperiodic_coefficient(self):
        expected = {i: self.V + self.V * np.cos(2 * np.pi * self.alpha * pos_i + self.delta) for i, (pos_i, _) in enumerate(self.interaction_coefficient.hopping_list)}
        self.assertEqual(self.interaction_coefficient.get_constant_vs_quasiperiodic_coefficient(), expected)

    def test_get_exponential_decay_coefficient(self):
        expected = {i: self.V * (abs(pos_i - pos_j)**(-6)) for i, (pos_i, pos_j) in enumerate(self.interaction_coefficient.hopping_list)}
        self.assertEqual(self.interaction_coefficient.get_exponential_decay_coefficient(), expected)


if __name__ == '__main__':
    unittest.main()
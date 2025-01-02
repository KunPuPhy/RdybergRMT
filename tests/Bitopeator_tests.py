import unittest
import sys
sys.path.append("../") # 
from rdybergrmt import *



class TestBitOperations(unittest.TestCase):
    def test_read_bit(self):
        self.assertEqual(read_bit(5, 0), 1)  # 5的二进制是101，第0位是1
        self.assertEqual(read_bit(5, 1), 0)  # 5的二进制是101，第1位是0
        self.assertEqual(read_bit(5, 2), 1)  # 5的二进制是101，第2位是1
        self.assertEqual(read_bit(8, 3), 1)  # 8的二进制是1000，第3位是1
        self.assertEqual(read_bit(8, 0), 0)  # 8的二进制是1000，第0位是0

    def test_flip_bit(self):
        self.assertEqual(flip_bit(5, 0), 4)  # 5的二进制是101，翻转第0位得到100
        self.assertEqual(flip_bit(5, 1), 7)  # 5的二进制是101，翻转第1位得到111
        self.assertEqual(flip_bit(5, 2), 1)  # 5的二进制是101，翻转第2位得到001
        self.assertEqual(flip_bit(8, 3), 0)  # 8的二进制是1000，翻转第3位得到0000
        self.assertEqual(flip_bit(8, 0), 9)  # 8的二进制是1000，翻转第0位得到1001

    def test_count_bit(self):
        self.assertEqual(count_bit(0), 0)  # 0的二进制是0，没有1
        self.assertEqual(count_bit(1), 1)  # 1的二进制是1，有一个1
        self.assertEqual(count_bit(3), 2)  # 3的二进制是11，有两个1
        self.assertEqual(count_bit(8), 1)  # 8的二进制是1000，有一个1
        self.assertEqual(count_bit(15), 4)  # 15的二进制是1111，有四个1


if __name__ == '__main__':
    unittest.main()
    
import task6_2
from unittest import TestCase

class TestPrime(TestCase):

    def setUp(self):
        """Init"""

    def test_diag1(self):
        """Test for daig1"""
        test1 = [[1, 2, 3], [2, 3, 4], [5, 6, 7]]
        test2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(task6_2.diag1(test1), 11)
        self.assertEqual(task6_2.diag1(test2), 0)

    def test_diag2(self):
        """Test for daig2"""
        test1 = [[1, 2, 3], [2, 3, 4], [5, 6, 7]]
        test2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(task6_2.diag2(test1), 11)
        self.assertEqual(task6_2.diag2(test2), 0)

    def test_res(self):
        """Test for res"""
        self.assertEqual(task6_2.res(5, 7), 2)
        self.assertEqual(task6_2.res(11, 11), 0)

    def tearDown(self):
        """Finish"""

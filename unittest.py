import unittest
from isPrime import is_prime

class Test(unittest.TestCase):
    def test_1(self):
        self.assertFalse(is_prime(1))

    def test_1(self):
        self.assertTrue(is_prime(2))

    def test_1(self):
        self.assertFalse(is_prime(8))

    def test_1(self):
        self.assertTrue(is_prime(11))

    def test_1(self):
        self.assertFalse(is_prime(1))

    def test_1(self):
        self.assertFalse(is_prime(1))

    def test_1(self):
        self.assertFalse(is_prime(1))
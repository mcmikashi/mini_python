import unittest

from package.fibonacci import fibonacci
from package.tribonacci import tribonacci
from package.lucas import lucas

class FibonacciTest(unittest.TestCase):

    def test_vide_zeros_un_deux(self):
        self.assertEqual(fibonacci(""), 0)
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)

    def test_basic(self):
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(8), 21)
        self.assertEqual(fibonacci(11), 89)
        self.assertEqual(fibonacci(16), 987)
        self.assertEqual(fibonacci(40), 102334155)
        self.assertEqual(fibonacci(64), 10610209857723)
        self.assertEqual(fibonacci(94), 19740274219868223167)
        self.assertEqual(
            fibonacci(200), 280571172992510140037611932413038677189525)

    def test_error(self):
        self.assertIsInstance(fibonacci("-1"), ValueError)
        self.assertIsInstance(fibonacci("aaaa"), ValueError)
        self.assertIsInstance(fibonacci(-100), ValueError)
        self.assertIsInstance(fibonacci(500), ValueError)

class TribonacciTest(unittest.TestCase):

    def test_vide_zeros_un_deux(self):
        self.assertEqual(tribonacci(""), 0)
        self.assertEqual(tribonacci(0), 0)
        self.assertEqual(tribonacci(1), 0)
        self.assertEqual(tribonacci(2), 1)

    def test_basic(self):
        self.assertEqual(tribonacci(3), 1)
        self.assertEqual(tribonacci(6), 7)
        self.assertEqual(tribonacci(9), 44)
        self.assertEqual(tribonacci(11), 149)
        self.assertEqual(tribonacci(16), 3136)
        self.assertEqual(tribonacci(28),  4700770)
        self.assertEqual(tribonacci(37),  1132436852)

    def test_error(self):
        self.assertIsInstance(tribonacci("-1"), ValueError)
        self.assertIsInstance(tribonacci("aaaa"), ValueError)
        self.assertIsInstance(tribonacci(-100), ValueError)
        self.assertIsInstance(tribonacci(500), ValueError)

class LucasNumbersTest(unittest.TestCase):

    def test_vide_zeros_un_deux(self):
        self.assertEqual(lucas(""), 2)
        self.assertEqual(lucas(0), 2)
        self.assertEqual(lucas(1), 1)
        self.assertEqual(lucas(2), 3)

    def test_basic(self):
        self.assertEqual(lucas(10), 123)
        self.assertEqual(lucas(14), 843)
        self.assertEqual(lucas(19), 9349)
        self.assertEqual(lucas(22), 39603)
        self.assertEqual(lucas(32), 4870847)
        self.assertEqual(lucas(35),  20633239)
        self.assertEqual(lucas(38),  87403803)

    def test_error(self):
        self.assertIsInstance(lucas("-1"), ValueError)
        self.assertIsInstance(lucas("aaaa"), ValueError)
        self.assertIsInstance(lucas(-100), ValueError)
        self.assertIsInstance(lucas(500), ValueError)

if __name__ == '__main__':
    unittest.main()
    
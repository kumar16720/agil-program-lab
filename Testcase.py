import unittest
import Calculator

class TestCalculation(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(2, 3), 5)
        self.assertEqual(Calculator.add(-1, 1), 0)
        self.assertEqual(Calculator.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(10, 5), 5)
        self.assertEqual(Calculator.subtract(10, 17), -7)
        self.assertEqual(Calculator.subtract(7, 0), 7)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(3, 4), 12)
        self.assertEqual(Calculator.multiply(-2, 5), -10)
        self.assertEqual(Calculator.multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(Calculator.divide(10, 2), 5)
        self.assertEqual(Calculator.divide(9, 3), 3)
        self.assertAlmostEqual(Calculator.divide(1, 3), 0.333333, places=5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            Calculator.divide(10, 0)

if __name__ == "__main__":
    unittest.main()
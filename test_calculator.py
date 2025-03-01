import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_square_root(self):
        self.assertAlmostEqual(calculator.square_root(16), 4)
        self.assertIsNone(calculator.square_root(-4))

    def test_factorial(self):
        self.assertEqual(calculator.factorial(5), 120)
        self.assertIsNone(calculator.factorial(-1))

    def test_natural_log(self):
        self.assertAlmostEqual(calculator.natural_log(1), 0)
        self.assertIsNone(calculator.natural_log(0))

    def test_power_function(self):
        self.assertAlmostEqual(calculator.power_function(2, 3), 8)
        self.assertAlmostEqual(calculator.power_function(9, 0.5), 3)

if __name__ == "__main__":
    unittest.main()
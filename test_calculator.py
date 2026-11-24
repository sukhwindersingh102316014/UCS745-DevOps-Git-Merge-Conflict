import unittest
from calculator import add, subtract, multiply, divide, power, square_root, percentage, modulo, calculate

class TestCalculatorUnified(unittest.TestCase):
    # Core arithmetic
    def test_add(self):
        self.assertEqual(add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        with self.assertRaises(ValueError):
            divide(10, 0)

    # Scientific operations
    def test_power(self):
        self.assertEqual(power(2, 4), 16)

    def test_square_root(self):
        self.assertEqual(square_root(25), 5)
        with self.assertRaises(ValueError):
            square_root(-4)

    # Financial operations
    def test_percentage(self):
        self.assertEqual(percentage(200, 15), 30.0)

    def test_modulo(self):
        self.assertEqual(modulo(10, 3), 1)
        with self.assertRaises(ValueError):
            modulo(10, 0)

    # Dispatcher
    def test_calculate_dispatcher(self):
        self.assertEqual(calculate("power", 3, 2), 9)
        self.assertEqual(calculate("modulo", 14, 5), 4)

if __name__ == "__main__":
    unittest.main()

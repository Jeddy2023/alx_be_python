import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Create an instance of SimpleCalculator before each test."""
        self.calc = SimpleCalculator()

    # Test for the add method
    def test_addition(self):
        """Test the addition method of SimpleCalculator."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(100, 50), 150)

    # Test for the subtract method
    def test_subtraction(self):
        """Test the subtraction method of SimpleCalculator."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    # Test for the multiply method
    def test_multiplication(self):
        """Test the multiplication method of SimpleCalculator."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(3, -3), -9)

    # Test for the divide method
    def test_division(self):
        """Test the division method of SimpleCalculator."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(3, 2), 1.5)
        self.assertEqual(self.calc.divide(5, -1), -5)
        self.assertIsNone(self.calc.divide(10, 0), "Expected None for division by zero")
        self.assertEqual(self.calc.divide(0, 1), 0)

if __name__ == "__main__":
    unittest.main()

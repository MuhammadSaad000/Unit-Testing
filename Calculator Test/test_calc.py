import unittest
import calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(3, 4), 7)
        self.assertEqual(calc.add(4, 5), 9)
        self.assertEqual(calc.add(0, -2), -2)

    def test_minus(self):
        self.assertEqual(calc.minus(3, 14), -11)
        self.assertEqual(calc.minus(4, 5), -1)
        self.assertEqual(calc.minus(0, -2), 2)

    def test_multiply(self):
        self.assertEqual(calc.multiply(3, 4), 12)
        self.assertEqual(calc.multiply(4, 5), 20)
        self.assertEqual(calc.multiply(0, -2), 0)

    def test_divide(self):
        self.assertEqual(calc.divide(8, 4), 2)
        self.assertEqual(calc.divide(84, 4), 21)
        self.assertEqual(calc.divide(0, -2), 0)

        # value error is handled in a different manner
        self.assertRaises(ValueError, calc.divide(10, 0))

        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()

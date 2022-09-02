from unittest import TestCase, main
from calculator import calculator
class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('2 + 2'), 4)
        self.assertEqual(calculator('8 - 6'), 2)
        self.assertEqual(calculator('4 * 5'), 20)
        self.assertEqual(calculator('9 / 3'), 3)


if __name__ == '__main__':
    main()   
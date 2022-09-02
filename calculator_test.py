from unittest import TestCase, main
from calculator import calculator
class CalculatorTest(TestCase):
    def test_fold(self):
        self.assertEqual(calculator('2 + 2'), 4)

    def test_subtract(self):
        self.assertEqual(calculator('8 - 6'), 2)
    
    def test_multiply(self):
        self.assertEqual(calculator('4 * 5'), 20)
    
    def test_divide(self):
        self.assertEqual(calculator('9 / 3'), 3)
    
    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('abracadabra')
        self.assertEqual('Выраженеие должно содержать хотя бы один знак (+-/*)', e.exception.args[0])

    def test_two_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('2 + 2 + 2')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])

    def test_many_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('2 + 3 * 5')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])

    def test_no_int(self):
        with self.assertRaises(ValueError) as e:
            calculator('2 + 3 * 5.0')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])

    def test_strings(self):
        with self.assertRaises(ValueError) as e:
            calculator('2 + b * a')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])

if __name__ == '__main__':
    main()   
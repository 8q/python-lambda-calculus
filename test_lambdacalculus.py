import unittest
from lambdacalculus import *


class TestLambdaCalculus(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(to_integer(ZERO), 0)

    def test_one(self):
        self.assertEqual(to_integer(ONE), 1)

    def test_two(self):
        self.assertEqual(to_integer(TWO), 2)

    def test_three(self):
        self.assertEqual(to_integer(THREE), 3)

    def test_four(self):
        self.assertEqual(to_integer(FOUR), 4)

    def test_five(self):
        self.assertEqual(to_integer(FIVE), 5)

    def test_true(self):
        self.assertEqual(to_boolean(TRUE), True)

    def test_false(self):
        self.assertEqual(to_boolean(FALSE), False)

    def test_and(self):
        self.assertEqual(to_boolean(AND(TRUE)(TRUE)), True)
        self.assertEqual(to_boolean(AND(TRUE)(FALSE)), False)
        self.assertEqual(to_boolean(AND(FALSE)(TRUE)), False)
        self.assertEqual(to_boolean(AND(FALSE)(FALSE)), False)

    def test_or(self):
        self.assertEqual(to_boolean(OR(TRUE)(TRUE)), True)
        self.assertEqual(to_boolean(OR(TRUE)(FALSE)), True)
        self.assertEqual(to_boolean(OR(FALSE)(TRUE)), True)
        self.assertEqual(to_boolean(OR(FALSE)(FALSE)), False)

    def test_not(self):
        self.assertEqual(to_boolean(NOT(TRUE)), False)
        self.assertEqual(to_boolean(NOT(FALSE)), True)

    def test_if(self):
        self.assertEqual(IF(TRUE)('happy')('sad'), 'happy')
        self.assertEqual(IF(FALSE)('happy')('sad'), 'sad')

    def test_is_zero(self):
        self.assertEqual(to_boolean(IS_ZERO(ZERO)), True)
        self.assertEqual(to_boolean(IS_ZERO(ONE)), False)

    def test_pair(self):
        my_pair = PAIR(THREE)(FIVE)
        self.assertEqual(to_integer(LEFT(my_pair)), 3)
        self.assertEqual(to_integer(RIGHT(my_pair)), 5)

    def test_increment(self):
        self.assertEqual(to_integer(INCREMENT(ZERO)), 1)
        self.assertEqual(to_integer(INCREMENT(FIVE)), 6)

    def test_slide(self):
        my_pair = SLIDE(PAIR(TWO)(THREE))
        self.assertEqual(to_integer(LEFT(my_pair)), 3)
        self.assertEqual(to_integer(RIGHT(my_pair)), 4)

    def test_decrement(self):
        self.assertEqual(to_integer(DECREMENT(ONE)), 0)
        self.assertEqual(to_integer(DECREMENT(FIVE)), 4)

    def test_add(self):
        self.assertEqual(to_integer(ADD(ONE)(TWO)), 3)
        self.assertEqual(to_integer(ADD(FIVE)(ZERO)), 5)
        self.assertEqual(to_integer(ADD(FIVE)(FIVE)), 10)

    def test_subtract(self):
        self.assertEqual(to_integer(SUBTRACT(TWO)(TWO)), 0)
        self.assertEqual(to_integer(SUBTRACT(FIVE)(ZERO)), 5)
        self.assertEqual(to_integer(SUBTRACT(FIVE)(ONE)), 4)

    def test_multiply(self):
        self.assertEqual(to_integer(MULTIPLY(TWO)(TWO)), 4)
        self.assertEqual(to_integer(MULTIPLY(FIVE)(ZERO)), 0)
        self.assertEqual(to_integer(MULTIPLY(FIVE)(FIVE)), 25)

    def test_power(self):
        self.assertEqual(to_integer(POWER(TWO)(TWO)), 4)
        self.assertEqual(to_integer(POWER(TWO)(ZERO)), 1)
        self.assertEqual(to_integer(POWER(FIVE)(THREE)), 125)

    def test_six(self):
        self.assertEqual(to_integer(SIX), 6)

    def test_seven(self):
        self.assertEqual(to_integer(SEVEN), 7)

    def test_eight(self):
        self.assertEqual(to_integer(EIGHT), 8)

    def test_nine(self):
        self.assertEqual(to_integer(NINE), 9)

    def test_ten(self):
        self.assertEqual(to_integer(TEN), 10)

    def test_fifteen(self):
        self.assertEqual(to_integer(FIFTEEN), 15)

    def test_hundred(self):
        self.assertEqual(to_integer(HUNDRED), 100)

    def test_is_less_or_equal(self):
        self.assertEqual(to_boolean(IS_LESS_OR_EQUAL(ONE)(TWO)), True)
        self.assertEqual(to_boolean(IS_LESS_OR_EQUAL(TWO)(TWO)), True)
        self.assertEqual(to_boolean(IS_LESS_OR_EQUAL(THREE)(TWO)), False)

    def test_mod(self):
        self.assertEqual(to_integer(MOD(THREE)(TWO)), 1)
        self.assertEqual(to_integer(
            MOD(POWER(THREE)(THREE))(ADD(TWO)(THREE))), 2)

    def test_list(self):
        my_list = UNSHIFT(
            UNSHIFT(
                UNSHIFT(EMPTY)(THREE)
            )(TWO)
        )(ONE)
        self.assertEqual([to_integer(n) for n in to_array(my_list)], [1, 2, 3])

    def test_length(self):
        self.assertEqual(to_integer(LENGTH(RANGE(ZERO)(TEN))), 11)

    def test_range(self):
        my_range = RANGE(ONE)(FIVE)
        self.assertEqual([to_integer(n)
                          for n in to_array(my_range)], [1, 2, 3, 4, 5])

    def test_fold(self):
        self.assertEqual(to_integer(
            FOLD(RANGE(ONE)(FIVE))(ZERO)(ADD)), 15)
        self.assertEqual(to_integer(
            FOLD(RANGE(ONE)(FIVE))(ONE)(MULTIPLY)), 120)

    def test_map(self):
        self.assertEqual([to_integer(n) for n in to_array(
            MAP(RANGE(ONE)(FIVE))(INCREMENT))], [2, 3, 4, 5, 6])

    def test_chars(self):
        self.assertEqual(to_char(ZERO), '0')
        self.assertEqual(to_char(A), 'A')
        self.assertEqual(to_char(Z), 'Z')

    def test_string(self):
        my_str = UNSHIFT(
            UNSHIFT(
                UNSHIFT(
                    UNSHIFT(EMPTY)(Z)
                )(Z)
            )(I)
        )(F)
        self.assertEqual(to_string(my_str), 'FIZZ')

    def test_div(self):
        self.assertEqual(to_integer(DIV(NINE)(TEN)), 0)
        self.assertEqual(to_integer(DIV(HUNDRED)(NINE)), 11)
        self.assertEqual(to_integer(DIV(HUNDRED)(TEN)), 10)

    def test_push(self):
        my_list = PUSH(
            PUSH(
                PUSH(EMPTY)(ONE)
            )(TWO)
        )(THREE)
        self.assertEqual([to_integer(n) for n in to_array(my_list)], [1, 2, 3])

    def test_to_digits(self):
        self.assertEqual([to_integer(n)
                          for n in to_array(TO_DIGITS(FIVE))], [5])
        self.assertEqual([to_integer(n)
                          for n in to_array(TO_DIGITS(POWER(FIVE)(THREE)))], [1, 2, 5])


if __name__ == '__main__':
    unittest.main()

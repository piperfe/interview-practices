import unittest

from src.shift_all_the_zeros_to_the_left import move_zeros_to_the_left


class ShiftAllTheZerosToTheLeftTestCase(unittest.TestCase):

    def test_move_one_zero_to_the_left_in_the_array(self):
        array_with_one_zero = [1, 2, 2, 0]

        array_with_zeros_to_the_left = move_zeros_to_the_left(array_with_one_zero)

        self.assertEqual([0, 2, 2, 1], array_with_zeros_to_the_left)

    def test_move_zeros_in_the_right_of_the_array_to_the_left(self):
        array_with_zeros_in_the_right_part_of_the_array = [1, 2, 2, 0, 0, 0]

        array_with_zeros_to_the_left = move_zeros_to_the_left(array_with_zeros_in_the_right_part_of_the_array)

        self.assertEqual([0, 0, 0, 1, 2, 2], array_with_zeros_to_the_left)

    def test_move_unorganized_zeros_to_the_left_in_the_array(self):
        array_with_unorganized_zeros = [0, 0, 2, 0, 1, 2]

        array_with_zeros_to_the_left = move_zeros_to_the_left(array_with_unorganized_zeros)

        self.assertEqual([0, 0, 0, 2, 1, 2], array_with_zeros_to_the_left)

    def test_do_not_move_the_zeros_in_an_array_with_the_zeros_in_the_left_already(self):
        array_with_zeros_in_the_left_already = [0, 0, 0, 2, 1, 2]

        array_with_zeros_to_the_left = move_zeros_to_the_left(array_with_zeros_in_the_left_already)

        self.assertEqual([0, 0, 0, 2, 1, 2], array_with_zeros_to_the_left)

    def test_do_not_move_the_zeros_in_an_array_with_one_zero_element(self):
        array_with_zero = [0]

        array_with_zeros_to_the_left = move_zeros_to_the_left(array_with_zero)

        self.assertEqual([0], array_with_zeros_to_the_left)

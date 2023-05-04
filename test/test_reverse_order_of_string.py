import unittest

from src.reverse_order_of_string import reverse_order


class ReverseOrderOfString(unittest.TestCase):

    def test_reverse_order_of_pair_string_characters(self):
        string_with_2_characters = 'lala'

        string_already_reversed = reverse_order(string_with_2_characters)

        self.assertEqual('alal', string_already_reversed)

    def test_reverse_order_of_impair_string_characters(self):
        string_with_2_characters = 'osol'

        string_already_reversed = reverse_order(string_with_2_characters)

        self.assertEqual('loso', string_already_reversed)

    def test_reverse_order_of_unique_string_character(self):
        string_with_2_characters = 'o'

        string_already_reversed = reverse_order(string_with_2_characters)

        self.assertEqual('o', string_already_reversed)

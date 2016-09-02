import unittest
from my_project import module_two


class BasicTestSuitePalindrome(unittest.TestCase):

    def test_module_two(self):
        expected = module_two.custom_count("AAAAsdfsdvver", 3)
        actual = [('A', 4)]
        self.assertEqual(expected, actual)

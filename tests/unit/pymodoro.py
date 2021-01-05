import unittest
from pymodoro import main


class UnitTests(unittest.TestCase):
    def test_test(self):
        self.assertEqual(main(), 'Ok')

import unittest
from pymodoro import main


class PymodoroUnitTests(unittest.TestCase):
    def test_test(self):
        self.assertEqual(main(), 'Ok')

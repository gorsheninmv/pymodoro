import unittest
from tomatorunner import config


class ConfigUnitTests(unittest.TestCase):
    def test_return_valid_config(self):
        self.assertTrue(not config.read())

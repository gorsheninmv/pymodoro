import unittest
from .unittests import pymodoro
from .unittests import tomatorunner

test_cases = [
        tomatorunner.ConfigUnitTests,
        pymodoro.PymodoroUnitTests,
        ]


def main():
    suite = unittest.TestSuite()
    tests = (unittest.defaultTestLoader.loadTestsFromTestCase(test_case)
             for test_case in test_cases)
    suite.addTests(tests)
    test_runner = unittest.TextTestRunner()
    test_runner.run(suite)

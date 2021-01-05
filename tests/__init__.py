import unittest
import itertools
from typing import Iterable
from . import integration
from .unit import pymodoro

unit_test_cases = [
        pymodoro.UnitTests
        ]

integration_test_cases = [
        integration.ConfigTests
        ]


def tests() -> None:
    all_test_cases = itertools.chain(unit_test_cases, integration_test_cases)
    tests = (unittest.defaultTestLoader.loadTestsFromTestCase(test_case)
             for test_case in all_test_cases)
    run_tests(tests)


def unit() -> None:
    tests = (unittest.defaultTestLoader.loadTestsFromTestCase(test_case)
             for test_case in unit_test_cases)
    run_tests(tests)


def run_tests(tests: Iterable[unittest.TestCase]) -> None:
    suite = unittest.TestSuite()
    suite.addTests(tests)
    test_runner = unittest.TextTestRunner()
    test_runner.run(suite)

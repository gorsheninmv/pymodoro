import unittest
import os
from pathlib import PurePath
from tomatorunner import config

tests_full_path = os.path.dirname(os.path.realpath(__file__))
fixtures_full_path = os.path.join(tests_full_path, 'fixtures')


class ConfigTests(unittest.TestCase):
    def test_return_valid_config(self):
        config_file_full_path = PurePath(fixtures_full_path, 'config.yaml')

        cfg = config.read(config_file_full_path)

        tomato_interval_mins = repr(config.Property.TomatoIntervalMins)
        self.assertEquals(cfg[tomato_interval_mins], 20)
        pause_interval_mins = str(config.Property.PauseIntervalMins)
        self.assertEquals(cfg[pause_interval_mins], 10)

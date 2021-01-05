import yaml
from enum import Enum
from pathlib import PurePath


def read(path: PurePath = None) -> dict:
    with open(path) as file:
        return yaml.load(file, Loader=yaml.Loader)


def write(config: dict) -> None:
    pass


class Property(Enum):
    def __str__(self):
        return self.value

    Nul = ''
    TomatoIntervalMins = 'tomato_interval_mins'
    PauseIntervalMins = 'pause_interval_mins'

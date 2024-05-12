import typing
from dataclasses import dataclass


class DemoPlainClass:
    a: int
    b: float = 1.1
    c = 'spam'


class DemoNTClass(typing.NamedTuple):
    a: int
    b: float = 1.1
    c = 'spam'


@dataclass
class DemoDataClass:
    a: int
    b: float = 1.1
    c = 'spam'

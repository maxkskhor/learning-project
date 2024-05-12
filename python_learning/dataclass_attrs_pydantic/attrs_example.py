from attrs import define, field, asdict


@define
class Coordinates:
    x: int
    y: int


c1 = Coordinates(1, 2)


@define
class C:
    x: int = field()

    @x.validator
    def check(self, attribute, value):
        if value > 42:
            raise ValueError("x must be smaller or equal to 42")

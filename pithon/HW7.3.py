from dataclasses import dataclass, asdict


def dataclass_with_asdict(cls):
    cls = dataclass(cls)
    cls.asdict = asdict
    return cls


@dataclass_with_asdict
class Point:
    x: int
    y: int


p = Point(9, 99)

print(p.asdict())

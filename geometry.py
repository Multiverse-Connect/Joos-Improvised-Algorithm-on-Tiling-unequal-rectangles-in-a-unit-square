from dataclasses import dataclass


@dataclass
class Rectangle:
    index: int
    width: float
    height: float


@dataclass
class Box:
    x: float
    y: float
    w: float
    h: float


@dataclass
class Placement:
    index: int
    x: float
    y: float
    width: float
    height: float
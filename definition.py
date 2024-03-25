import os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


def lerp(v0: float, v1: float, t: float) -> float:
    return (1 - t) * v0 + t * v1

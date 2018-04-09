"""Provides access to mathematical functions"""


def distance(x1, y1, x2, y2):
    """Calculates a distance between given points"""
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

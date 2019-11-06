"""
test_python.py почему-то не проходит pytest.
"""
from math import pi, sqrt, pow, hypot


def test_filter():
    assert list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])) == [2, 4]  # все четные


def test_map():
    assert list(map(lambda x: x + 1, [1, 2, 3, 4, 5])) == [2, 3, 4, 5, 6]  # на единичку больше


def test_sorted():
    assert list(sorted([5, 3, 4, 1, 2])) == [1, 2, 3, 4, 5]  # отсортировано по возрастанию


def test_pi():
    assert pi < 4  # число пи меньше четырех = истина


def test_sqrt():
    assert sqrt(4) == 2


def test_pow():
    assert pow(2, 2) == 4


def test_hypot():
    assert hypot(3, 4) == 5  # теорема Ферма для n=2

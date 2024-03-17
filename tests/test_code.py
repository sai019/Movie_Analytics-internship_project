import pytest


def add(a, b):
    return a + b


def test_add():
    assert add(1, 2) == 3


def test_add_negative_numbers():
    assert add(-1, -1) == -2


def test_add_zero():
    assert add(0, 0) == 0


if __name__ == "__main__":
    pytest.main()

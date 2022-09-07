import os
import sys

import pytest

from spc.rectangular import Rectangular
from pytest_subtests import subtests
HEIGHT = 100
WIDTH = 50

@pytest.fixture
def rectangular():
    return Rectangular(HEIGHT, WIDTH)


def teardown_function():
    print("I open at the close")


def test_area(rectangular):
    assert rectangular.area == HEIGHT*WIDTH


def test_resize(subtests, rectangular):

    for i in range(5):
        with subtests.test(scale = i):
            rectangular.resize(i*HEIGHT, i*WIDTH)
            assert rectangular.width == i*WIDTH
            assert rectangular.height == i*HEIGHT

    for pair in [(-10, 10), (10, -10)]:
        with subtests.test(pair = pair):
            with pytest.raises(ValueError):
                rectangular.resize(*pair)

    for pair in [(10, 10.0), (10.0, 10)]:
        with subtests.test(pair = pair):
            with pytest.raises(TypeError):
                rectangular.resize(*pair)


@pytest.skip("", allow_module_level=True)
def test_rotation(rectangular):
    rectangular.rotate()
    assert rectangular.height == WIDTH
    assert rectangular.width == HEIGHT


@pytest.mark.skipif(sys.platform.startswith("win"), "requires Windows")
def test_system(self):
    os.system("ls")



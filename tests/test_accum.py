import pytest
from stuff.accum import Accumulator

@pytest.fixture
def accum():
    return Accumulator()

def test_accumulator_init_fixture(accum):
    assert accum.count == 0

def test_accumulator_init():
    accum = Accumulator()
    assert accum.count == 0


def test_accumulator_add_one():
    accum = Accumulator()
    accum.add()
    assert accum.count == 1

def test_accumulator_add_one_fixture(accum):
    accum.add()
    assert accum.count == 1

def test_accumulator_add_three():
    accum = Accumulator()
    accum.add(3)
    assert accum.count == 3

def test_accumulator_add_three_fixture(accum):
    accum.add(3)
    assert accum.count == 3

def test_accumulator_cannot_set_count_directly():
    accum = Accumulator()
    with pytest.raises(AttributeError, match="can't set attribute") as e:
        accum.count = 10

def test_accumulator_cannot_set_count_directly_fixture(accum):
    with pytest.raises(AttributeError, match="can't set attribute") as e:
        accum.count = 10
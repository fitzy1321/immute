import pytest
from immute import Immutable


class Thing(Immutable):
    def __init__(self) -> None:
        self.num = 42


def test_reassignment_raises_type_error():
    thing = Thing()
    with pytest.raises(TypeError):
        thing.num = 21


def test_new_assignmnet_raises_type_error():
    thing = Thing()
    with pytest.raises(TypeError):
        thing.m_str = "Something..."


def test_del_raises_type_error():
    with pytest.raises(TypeError):
        thing = Thing()
        del thing.num


def test_assignmnet_to_class_raises_type_error():
    with pytest.raises(TypeError) as e:
        Thing.m_str = "Something ..."

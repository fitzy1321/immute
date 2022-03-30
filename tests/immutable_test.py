import pytest
from immute import Immutable

NUM = 42


class Thing(Immutable):
    class_var = "Does this work?"

    def __init__(self) -> None:
        self.num = NUM


def test_class_init_still_works():
    thing = Thing()
    assert thing.num == NUM


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


def test_class_variable_assignmnet_outside_class_def_raises_type_error():
    with pytest.raises(TypeError):
        Thing.m_str = "Something ..."


def test_class_variable_assignment_in_class_def_still_works():
    try:
        if Thing.class_var:
            assert True
    except Exception:
        assert False


def test_class_variable_del_raises_type_error():
    with pytest.raises(TypeError):
        del Thing.class_var

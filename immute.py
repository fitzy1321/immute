import inspect

_SAFE_MUT_FUNCS = ("__init__", "__new__")


def _delattr(self) -> None:
    raise TypeError(
        f"Objects of type '{type(self).__name__}' are immutable, "
        "and do not support assignments or reassignment operations."
    )


def _setattr(self, *args) -> None:
    # Use inspect to traverse function stacks
    # First func should be __settatr__
    # Second func should be init or new
    prev_func = inspect.stack()[2][3]
    if prev_func in _SAFE_MUT_FUNCS:
        object.__setattr__(self, *args)
    else:
        raise TypeError(
            f"Objects of type '{type(self).__name__}' are immutable, "
            "and do not support assignments or reassignment operations."
        )


class ImmutableMeta(type):
    def __delattr__(self, *args) -> None:
        _delattr(self)

    def __setattr__(self, *args) -> None:
        _setattr(self, *args)


class Immutable(metaclass=ImmutableMeta):
    def __delattr__(self, *args) -> None:
        _delattr(self)

    def __setattr__(self, *args) -> None:
        _setattr(self, *args)

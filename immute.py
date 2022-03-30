import inspect


class ImmutableMeta(type):
    def __delattr__(self, *args) -> None:
        raise TypeError(
            f"Objects derived from '{type(self).__name__}' are immutable, "
            "and do not support deletions."
        )

    def __setattr__(self, *args) -> None:
        if inspect.stack()[1][3] in ("__init__", "__new__"):
            object.__setattr__(self, *args)
        else:
            raise TypeError(
                f"Objects of type '{type(self).__name__}' are immutable, "
                "and do not support assignments or reassignment operations."
            )


class Immutable(metaclass=ImmutableMeta):
    def __delattr__(self, *args) -> None:
        raise TypeError(
            f"Objects of type '{type(self).__name__}' are immutable, "
            "and do not support deletions."
        )

    def __setattr__(self, *args) -> None:
        if inspect.stack()[1][3] == "__init__":
            object.__setattr__(self, *args)
        else:
            raise TypeError(
                f"Objects of type '{type(self).__name__}' are immutable, "
                "and do not support assignments or reassignment operations."
            )

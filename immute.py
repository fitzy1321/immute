import inspect
from typing import Any


class ImmutableMeta(type):
    def __delattr__(self, __name: str) -> None:
        raise TypeError(
            f"Objects of type '{type(self).__name__}' are immutable, "
            "and do not support deletions."
        )

    def __setattr__(self, __name: str, __value: Any) -> None:
        print(inspect.stack()[1][3])
        if inspect.stack()[1][3] in ("__init__", "__new__"):
            object.__setattr__(self, __name, __value)
        else:
            raise TypeError(
                f"Objects of type '{type(self).__name__}' are immutable, "
                "and do not support assignments."
            )


class Immutable(metaclass=ImmutableMeta):
    def __delattr__(self, __name: str) -> None:
        raise TypeError(
            f"Objects of type '{type(self).__name__}' are immutable, "
            "and do not support deletions."
        )

    def __setattr__(self, __name: str, __value: Any) -> None:
        if inspect.stack()[1][3] == "__init__":
            object.__setattr__(self, __name, __value)
        else:
            raise TypeError(
                f"Objects of type '{type(self).__name__}' are immutable, "
                "and do not support assignments."
            )

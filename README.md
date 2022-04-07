# Immute

Create "immutable" classes in python.

I created a simple python object that, when inherited in another class, will prevent assignment operations outside the `__init__()` or `__new__()` methods.

**Note: DOES NOT CREATE TRUELY IMMUTABLE REFERENCES.**

Classes inheriting from `Immutable` are not immutable references, only immutable from assignments, reassignment and deletion operations.

Classes inheriting from `Immutable` are still mutable reference types, and not truly immutable like python's built-in types (int, float, bool, str, tuples).

## Example

```python
from immute import Immutable

class Singleton(Immutable):
    _instance = None # Class fields allowed during class definition

    # __new__() and __init__() methods are allowed to modify class state.
    # After instantiation, setattr and delattr are effectively ''disabled'
    def __new__(cls, *args, **kwargs) -> Singleton:
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self) -> None:
        self.num = 42
        self.title = "My Super Cool App!"

config = Singleton()
print(config.title)

config.num = 21

# ^^^^^^ This will raise a TypeError exception
#
# Attempting to assign class level attributes will throw an error
Singleton.name = "thing 1"
# ^^^^^^^^ This will raise a TypeError exception
```

## To Install

To install this package, enter on of the following

`pip install immute`

or

`poetry add immute`

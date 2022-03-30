# Immute

Create "immutable" classes in python.

I created a simple python object that, when inherited in another class, will prevent assignment operations outside the `\_\_init__()` method.

**Note: DOES NOT CREATE TRUELY IMMUTABLE REFERENCES**

Classes inheriting from `Immutable` are not immutable references, only immutable from assignments, reassignment and deletion operations.

Classes inheriting from `Immutable` are still mutable reference types, and not truly immutable like python's built-in types (int, float, bool, str, tuples).

## Example

```python
from immute import Immutable

class Thing(Immutable):
    def __init__(self) -> None:
        self.num = 42

thing = Thing()

thing.num = 21
# ^^^^^^ This will raise a TypeError exception
```

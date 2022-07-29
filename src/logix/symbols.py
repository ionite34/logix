# Symbols for Logix
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Symbol:
    """Symbol for Logic Operations."""
    name: str
    _value: bool | None = field(default=None, init=False)

    def __post_init__(self) -> None:
        """Check if name is a valid symbol."""
        if not isinstance(self.name, str):
            raise TypeError("Symbol name must be a string.")

    @property
    def value(self) -> bool | None:
        """Return value of symbol."""
        if self._value is None:
            raise ValueError("Symbol value is not set.")
        return self._value

    @value.setter
    def value(self, value: bool) -> None:
        """Set value of symbol."""
        self._value = bool(value)


def symbols(*names: str) -> tuple[Symbol, ...]:
    """Create Multiple Symbols."""
    # If names is a single string, parse for commas
    if len(names) == 1:
        names = tuple(names[0].split(","))

    return tuple(Symbol(name) for name in names)

from __future__ import annotations

from dataclasses import dataclass

from symbols import Symbol


@dataclass
class Expression:
    seq: str


class Logic:
    """Logical Expressions."""

    def __init__(self, symbol: str) -> None:
        """Initialize Logic Expression."""
        # Holds all Symbols
        self._symbols: set[Symbol] = {Symbol(symbol)}
        # Expression
        self._exp = Expression(symbol)

    @classmethod
    def from_expression(cls, exp: Expression) -> Logic:
        """Creates a Logic from Expression."""

        exp

    def __neg__(self) -> Logic:
        """Negate Logic Expression."""
        res = self.copy()
        return Logic(f"~{self._exp}")

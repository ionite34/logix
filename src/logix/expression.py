from __future__ import annotations

from symbols import Symbol


class Logic:
    """Logical Expressions."""

    def __init__(self, symbol: str) -> None:
        """Initialize Logic Expression."""
        # Build symbol
        sym = Symbol(symbol)
        # Holds all Symbols
        self.symbols: set[Symbol] = {sym}

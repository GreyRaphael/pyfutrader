from typing import Protocol
from datatype import quote


# define a interface
class StrategyBase(Protocol):
    def on_bar(self, bar: quote.TickData) -> None: ...

    def on_tick(self, tick: quote.TickData) -> None: ...

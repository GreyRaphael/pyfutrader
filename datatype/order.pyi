import ctypes
from typing import ClassVar

class Order(ctypes.Structure):
    _fields_: ClassVar[list[tuple[str, type]]]

    stg_name: bytes
    symbol: bytes
    stamp: int
    volume: int
    direction: int
    offset: int

    def to_dict(self) -> dict: ...

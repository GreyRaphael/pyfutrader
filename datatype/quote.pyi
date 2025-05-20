import ctypes
from typing import ClassVar

class TickData(ctypes.Structure):
    _fields_: ClassVar[list[tuple[str, type]]]

    symbol: bytes
    stamp: int
    open: float
    high: float
    low: float
    last: float
    close: float
    settle: float
    limit_up: float
    limit_down: float
    preclose: float
    presettle: float
    volume: float
    amount: float
    oi: float
    preoi: float
    avgprice: float
    adj: float
    ap1: float
    ap2: float
    ap3: float
    ap4: float
    ap5: float
    bp1: float
    bp2: float
    bp3: float
    bp4: float
    bp5: float
    av1: int
    av2: int
    av3: int
    av4: int
    av5: int
    bv1: int
    bv2: int
    bv3: int
    bv4: int
    bv5: int

    def to_dict(self) -> dict: ...

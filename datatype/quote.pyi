import ctypes
from typing import ClassVar

class TickData(ctypes.Structure):
    _fields_: ClassVar[list[tuple[str, type]]]

    TradingDay: bytes
    reserve1: bytes
    ExchangeID: bytes
    reserve2: bytes
    LastPrice: float
    PreSettlementPrice: float
    PreClosePrice: float
    PreOpenInterest: float
    OpenPrice: float
    HighestPrice: float
    LowestPrice: float
    Volume: int
    Turnover: float
    OpenInterest: float
    ClosePrice: float
    SettlementPrice: float
    UpperLimitPrice: float
    LowerLimitPrice: float
    PreDelta: float
    CurrDelta: float
    UpdateTime: bytes
    UpdateMillisec: int
    BidPrice1: float
    BidVolume1: int
    AskPrice1: float
    AskVolume1: int
    BidPrice2: float
    BidVolume2: int
    AskPrice2: float
    AskVolume2: int
    BidPrice3: float
    BidVolume3: int
    AskPrice3: float
    AskVolume3: int
    BidPrice4: float
    BidVolume4: int
    AskPrice4: float
    AskVolume4: int
    BidPrice5: float
    BidVolume5: int
    AskPrice5: float
    AskVolume5: int
    AveragePrice: float
    ActionDay: bytes
    InstrumentID: bytes
    ExchangeInstID: bytes
    BandingUpperPrice: float
    BandingLowerPrice: float

    def to_dict(self) -> dict: ...

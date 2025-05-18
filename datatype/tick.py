import ctypes


class CThostFtdcDepthMarketDataField(ctypes.Structure):
    _fields_ = [
        ("TradingDay", ctypes.c_char * 9),
        ("reserve1", ctypes.c_char * 31),
        ("ExchangeID", ctypes.c_char * 9),
        ("reserve2", ctypes.c_char * 31),
        ("LastPrice", ctypes.c_double),
        ("PreSettlementPrice", ctypes.c_double),
        ("PreClosePrice", ctypes.c_double),
        ("PreOpenInterest", ctypes.c_double),
        ("OpenPrice", ctypes.c_double),
        ("HighestPrice", ctypes.c_double),
        ("LowestPrice", ctypes.c_double),
        ("Volume", ctypes.c_int),
        ("Turnover", ctypes.c_double),
        ("OpenInterest", ctypes.c_double),
        ("ClosePrice", ctypes.c_double),
        ("SettlementPrice", ctypes.c_double),
        ("UpperLimitPrice", ctypes.c_double),
        ("LowerLimitPrice", ctypes.c_double),
        ("PreDelta", ctypes.c_double),
        ("CurrDelta", ctypes.c_double),
        ("UpdateTime", ctypes.c_char * 9),
        ("UpdateMillisec", ctypes.c_int),
        ("BidPrice1", ctypes.c_double),
        ("BidVolume1", ctypes.c_int),
        ("AskPrice1", ctypes.c_double),
        ("AskVolume1", ctypes.c_int),
        ("BidPrice2", ctypes.c_double),
        ("BidVolume2", ctypes.c_int),
        ("AskPrice2", ctypes.c_double),
        ("AskVolume2", ctypes.c_int),
        ("BidPrice3", ctypes.c_double),
        ("BidVolume3", ctypes.c_int),
        ("AskPrice3", ctypes.c_double),
        ("AskVolume3", ctypes.c_int),
        ("BidPrice4", ctypes.c_double),
        ("BidVolume4", ctypes.c_int),
        ("AskPrice4", ctypes.c_double),
        ("AskVolume4", ctypes.c_int),
        ("BidPrice5", ctypes.c_double),
        ("BidVolume5", ctypes.c_int),
        ("AskPrice5", ctypes.c_double),
        ("AskVolume5", ctypes.c_int),
        ("AveragePrice", ctypes.c_double),
        ("ActionDay", ctypes.c_char * 9),
        ("InstrumentID", ctypes.c_char * 81),
        ("ExchangeInstID", ctypes.c_char * 81),
        ("BandingUpperPrice", ctypes.c_double),
        ("BandingLowerPrice", ctypes.c_double),
    ]

    def __repr__(self):
        parts = []
        for name, _ in self._fields_:
            val = getattr(self, name)
            parts.append(f"{name}={val}")
        return f"{self.__class__.__name__}({', '.join(parts)})"

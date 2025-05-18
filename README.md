# pyfutrader

python futures trader


## python struct vs ctypes

> ctypes is recommended!

```py
import struct
import ctypes

# method 1: with struct
# CThostFtdcDepthMarketDataField
# <   : little-endian, standard sizes, no alignment
# @   : do exactly the same padding that your C compiler does
# 9s  : char[9]
# 31s : char[31]
# 81s : char[81]
# d   : double (8 bytes)
# i   : int    (4 bytes)
MD_STRUCT_FMT = "@" + "9s" + "31s" + "9s" + "31s" + "7d" + "i" + "8d" + "9s" + "i" + "di" * 10 + "d" + "9s" + "81s" + "81s" + "2d"

binary_msg = b"20250516\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00CZCE\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\xa2@\x00\x00\x00\x00\x00@\xa2@\x00\x00\x00\x00\x00 \xa2@\x00\x00\x00\x00\xdch&A\x00\x00\x00\x00\x00\x16\xa2@\x00\x00\x00\x00\x00(\xa2@\x00\x00\x00\x00\x00\x06\xa2@e\x99\x04\x00\x00\x00\x00\x00\x00\x00\x00\xde\xde\xcd\xc4A\x00\x00\x00\x00\xf2q&A\x00\x00\x00\x00\x00\x18\xa2@\x00\x00\x00\x00\x00\x18\xa2@\x00\x00\x00\x00\x00\x88\xa3@\x00\x00\x00\x00\x00\xf8\xa0@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0009:44:40\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\xa2@\x16\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1a\xa2@i\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0020250516\x00MA509\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"

(
    TradingDay,
    reserve1,
    ExchangeID,
    reserve2,
    LastPrice,
    PreSettlementPrice,
    PreClosePrice,
    PreOpenInterest,
    OpenPrice,
    HighestPrice,
    LowestPrice,
    Volume,
    Turnover,
    OpenInterest,
    ClosePrice,
    SettlementPrice,
    UpperLimitPrice,
    LowerLimitPrice,
    PreDelta,
    CurrDelta,
    UpdateTime,
    UpdateMillisec,
    BidPrice1,
    BidVolume1,
    AskPrice1,
    AskVolume1,
    BidPrice2,
    BidVolume2,
    AskPrice2,
    AskVolume2,
    BidPrice3,
    BidVolume3,
    AskPrice3,
    AskVolume3,
    BidPrice4,
    BidVolume4,
    AskPrice4,
    AskVolume4,
    BidPrice5,
    BidVolume5,
    AskPrice5,
    AskVolume5,
    AveragePrice,
    ActionDay,
    InstrumentID,
    ExchangeInstID,
    BandingUpperPrice,
    BandingLowerPrice,
) = struct.unpack(MD_STRUCT_FMT, binary_msg)
print(TradingDay)

# method 2: with ctypes
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

tick=CThostFtdcDepthMarketDataField.from_buffer_copy(binary_msg)
print(tick)
```
import ctypes


# CThostFtdcDepthMarketDataField
class TickData(ctypes.Structure):
    _fields_ = [
        ("symbol", ctypes.c_char * 32),
        ("stamp", ctypes.c_int64),
        ("open", ctypes.c_double),
        ("high", ctypes.c_double),
        ("low", ctypes.c_double),
        ("last", ctypes.c_double),
        ("limit_down", ctypes.c_double),
        ("limit_up", ctypes.c_double),
        ("preclose", ctypes.c_double),
        ("close", ctypes.c_double),
        ("presettle", ctypes.c_double),
        ("settle", ctypes.c_double),
        ("preoi", ctypes.c_double),
        ("oi", ctypes.c_double),
        ("volume", ctypes.c_int64),
        ("amount", ctypes.c_double),
        ("avgprice", ctypes.c_double),
        ("ap1", ctypes.c_double),
        ("ap2", ctypes.c_double),
        ("ap3", ctypes.c_double),
        ("ap4", ctypes.c_double),
        ("ap5", ctypes.c_double),
        ("bp1", ctypes.c_double),
        ("bp2", ctypes.c_double),
        ("bp3", ctypes.c_double),
        ("bp4", ctypes.c_double),
        ("bp5", ctypes.c_double),
        ("av1", ctypes.c_int32),
        ("av2", ctypes.c_int32),
        ("av3", ctypes.c_int32),
        ("av4", ctypes.c_int32),
        ("av5", ctypes.c_int32),
        ("bv1", ctypes.c_int32),
        ("bv2", ctypes.c_int32),
        ("bv3", ctypes.c_int32),
        ("bv4", ctypes.c_int32),
        ("bv5", ctypes.c_int32),
        ("adj", ctypes.c_double),
    ]

    def __repr__(self):
        parts = []
        for name, _ in self._fields_:
            val = getattr(self, name)
            parts.append(f"{name}={val}")
        return f"{self.__class__.__name__}({', '.join(parts)})"

    def to_dict(self):
        return {name: getattr(self, name) for name, _ in self._fields_}

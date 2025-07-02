import ctypes


class Order(ctypes.Structure):
    _fields_ = [
        ("stg_name", ctypes.c_char * 32),
        ("symbol", ctypes.c_char * 16),
        ("stamp", ctypes.c_int64),
        ("volume", ctypes.c_uint32),
        ("direction", ctypes.c_uint8),
        ("offset", ctypes.c_uint8),
    ]

    def __repr__(self):
        parts = []
        for name, _ in self._fields_:
            val = getattr(self, name)
            parts.append(f"{name}={val}")
        return f"{self.__class__.__name__}({', '.join(parts)})"

    def to_dict(self):
        return {name: getattr(self, name) for name, _ in self._fields_}

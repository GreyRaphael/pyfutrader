from config import utils
import pynng
from datatype import quote
from ta import rolling


def main():
    smaer = rolling.Meaner(5)

    nng_config = utils.read_config("config/nng.toml")
    # empty topics to receive all messages
    with pynng.Sub0(dial=nng_config["Address"], topics=b"") as sub:
        while True:
            binary_msg = sub.recv()
            tick = quote.TickData.from_buffer_copy(binary_msg)
            print(tick.InstrumentID, f"{tick.TradingDay + b' ' + tick.UpdateTime}.{tick.UpdateMillisec}", tick.LastPrice)
            # print(tick.to_dict())
            ma5 = smaer.update(tick.LastPrice)
            print(f"======>ma5={ma5}")


if __name__ == "__main__":
    main()

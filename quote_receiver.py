from config import utils
import pynng
from datatype import quote
from ta import rolling
import datetime as dt


def main():
    smaer = rolling.Meaner(5)

    nng_config = utils.read_config("config/nng.toml")
    # empty topics to receive all messages
    sub = pynng.Sub0(topics=b"")
    # do a non-blocking dial: no exception if nobody is listening yet!
    sub.dial(nng_config["Address"], block=False)
    with sub:
        while True:
            binary_msg = sub.recv()
            tick = quote.TickData.from_buffer_copy(binary_msg)
            tick_dt = dt.datetime.fromtimestamp(tick.stamp / 1000.0)
            print(tick_dt, tick.symbol, tick.last)
            # print(tick)
            # print(tick.to_dict())
            ma5 = smaer.update(tick.last)
            print(f"======>ma5={ma5}")


if __name__ == "__main__":
    main()

from config import utils
import pynng
from datatype import quote


def main():
    nng_config = utils.read_config("config/nng.toml")
    # empty topics to receive all messages
    with pynng.Sub0(dial=nng_config["Address"], topics=b"") as sub:
        while True:
            binary_msg = sub.recv()
            tick = quote.TickData.from_buffer_copy(binary_msg)
            print(tick)
            print(tick.to_dict())


if __name__ == "__main__":
    main()

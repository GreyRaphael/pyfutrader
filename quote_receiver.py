import tomllib
import pynng
from datatype import quote


def read_config(filename: str) -> dict:
    with open(filename, "rb") as file:
        config_dict = tomllib.load(file)
    return config_dict


def main():
    nng_config = read_config("config/nng.toml")
    # empty topics to receive all messages
    with pynng.Sub0(dial=nng_config["Address"], topics=b"") as sub:
        while True:
            binary_msg = sub.recv()
            tick = quote.TickData.from_buffer_copy(binary_msg)
            print(tick)


if __name__ == "__main__":
    main()

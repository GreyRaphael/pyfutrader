from config import utils
import zmq
from datatype import quote
from ta import rolling
import datetime as dt


def main():
    smaer = rolling.Meaner(5)

    nng_config = utils.read_config("config/nng.toml")

    context = zmq.Context()
    subscriber = context.socket(zmq.SUB)

    # Set high-water mark for inbound messages
    subscriber.set(zmq.RCVHWM, 0)

    # Subscribe to topic 'rb'
    subscriber.set(zmq.SUBSCRIBE, b"")

    # Non-blocking connect (equivalent to NNG's block=False)
    try:
        subscriber.connect(nng_config["Address"])
    except zmq.ZMQError as e:
        print(f"Connection error: {e}")

    count = 0
    while True:
        try:
            binary_msg = subscriber.recv()
            tick = quote.TickData.from_buffer_copy(binary_msg)
            tick_dt = dt.datetime.fromtimestamp(tick.stamp / 1000.0)
            print(tick_dt, tick.symbol, tick.last)
            count += 1
            ma5 = smaer.update(tick.last)
            print(f"======>ma5={ma5},count={count}")
        except zmq.Again:
            continue  # Non-blocking retry or add delay


if __name__ == "__main__":
    main()

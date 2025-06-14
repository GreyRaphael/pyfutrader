import os
import zmq
import datetime as dt
import polars as pl
from config import utils
from datatype import quote


def main():
    config = utils.read_config("config/zmq.toml")

    context = zmq.Context()
    subscriber = context.socket(zmq.SUB)

    # Set high‐water mark for inbound messages
    subscriber.set(zmq.RCVHWM, 0)
    subscriber.set(zmq.SUBSCRIBE, b"")

    try:
        subscriber.connect(config["Address"])
    except zmq.ZMQError as e:
        print(f"Connection error: {e}")
        return

    # ========== CONFIGURATION ==========
    BATCH_SIZE = 10000
    FLUSH_INTERVAL = 300  # seconds,  periodic flushes
    output_dir = dt.date.today().strftime("data/%Y%m%d")
    os.makedirs(output_dir, exist_ok=True)

    buffer: list[dict] = []  # will hold up to BATCH_SIZE rows before writing
    batch_idx = 0
    last_flush_time = dt.datetime.now()
    # ===================================

    try:
        while True:
            # (this recv() blocks by default; if you want it nonblocking,
            #  you can set RCVTIMEO and catch zmq.Again, but for simplicity
            #  we'll keep it blocking here.)
            binary_msg = subscriber.recv()
            tick = quote.TickData.from_buffer_copy(binary_msg)

            # Extract the fields you want to store
            # (e.g. as a tuple: (datetime, symbol, last_price))
            buffer.append(tick.to_dict())

            now = dt.datetime.now()
            # Once we hit BATCH_SIZE entries, flush to Parquet
            if len(buffer) >= BATCH_SIZE or (now - last_flush_time).total_seconds() >= FLUSH_INTERVAL:
                batch_idx += 1
                filename = os.path.join(output_dir, f"ticks_{batch_idx:04d}.parquet")

                # Build a Polars DataFrame from the list of dicts
                df = pl.DataFrame(buffer)

                # Write to Parquet (default compression = "snappy")
                df.write_parquet(filename, compression="zstd", compression_level=10)
                last_flush_time = now

                print(f"Wrote batch {batch_idx} ({len(buffer)} rows) → {filename}")

                # Clear the buffer for the next batch
                buffer.clear()

    except KeyboardInterrupt:
        # On CTRL+C (or any clean shutdown), write out any remaining rows
        if buffer:
            batch_idx += 1
            filename = os.path.join(output_dir, f"ticks_{batch_idx:04d}.parquet")
            df = pl.DataFrame(buffer)
            df.write_parquet(filename, compression="zstd", compression_level=10)
            print(f"\nShutdown: wrote final batch {batch_idx} ({len(buffer)} rows) → {filename}")

            # Close the subscriber and context
            subscriber.close()
            context.term()

        print("Exiting.")


if __name__ == "__main__":
    main()

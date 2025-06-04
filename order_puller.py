import zmq
from datatype import order


def main():
    context = zmq.Context()
    puller = context.socket(zmq.PULL)
    puller.bind("ipc://@orders")

    try:
        while True:
            binary_msg = puller.recv()
            o = order.Order.from_buffer_copy(binary_msg)
            print(o.to_dict())
    except KeyboardInterrupt:
        print("\nInterrupted, closing socket…")
    finally:
        puller.close()
        context.term()


if __name__ == "__main__":
    main()

import zmq
import random
import time

# Create a ZeroMQ context
context = zmq.Context()

# Create a socket to receive requests from the main app
socket = context.socket(zmq.REP)  # Reply socket
socket.bind("tcp://*:5558")  # Bind to a specific port


def generate_random_delay(time_range):
    """
    Generate a random delay within the specified time range.

    :param time_range: List with two elements [min_time, max_time]
    :return: Random delay within the specified range
    """
    min_time, max_time = time_range
    return random.uniform(min_time, max_time)


while True:
    # Wait for a request from the main app
    time_range = socket.recv_pyobj()
    print(f"Received request for delay range: {time_range}")

    # Generate random delay
    delay = generate_random_delay(time_range)
    print(f"Generated warp delay: {delay:.2f} seconds")

    # Send the delay back to the main app
    socket.send_pyobj(delay)

context.destroy()

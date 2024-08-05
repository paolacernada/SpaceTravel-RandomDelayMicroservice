"""
test_random_delay.py

This script tests the random delay microservice for generating random time delays
within a specified range. It simulates interaction with the microservice using
ZeroMQ sockets, similar to how a space exploration application might use the service.

The test program requests random delays and verifies that the microservice returns
valid delay times. It also simulates the delay in the application flow using space
travel terminology.

To run this test program, ensure that the random delay microservice is running.
"""

import zmq
import time


def setup_zeromq():
    """
    Set up ZeroMQ context and request socket for communicating with the microservice.

    :return: ZeroMQ socket connected to the microservice
    """
    # Create a ZeroMQ context
    context = zmq.Context()

    # Create a socket to request random delays
    random_delay_socket = context.socket(zmq.REQ)
    random_delay_socket.connect("tcp://localhost:5558")  # Connect to your microservice

    return random_delay_socket


def request_random_delay(socket, time_range):
    """
    Send a request to the microservice with a specified time range and receive the random delay.

    :param socket: ZeroMQ socket connected to the microservice
    :param time_range: List containing the minimum and maximum delay time
    :return: Random delay received from the microservice
    """
    print(f"Requesting warp charge delay with range: {time_range}")

    # Send the time range to the microservice
    socket.send_pyobj(time_range)

    # Receive the random delay from the microservice
    warp_delay = socket.recv_pyobj()
    print(f"Warp delay received: {warp_delay:.2f} seconds\n")

    return warp_delay


def simulate_space_exploration(warp_delay):
    """
    Simulate the delay in the space exploration process using the received delay.

    :param warp_delay: Delay time in seconds
    """
    print("Initiating warp drive charging sequence...")
    time.sleep(warp_delay)  # Use the received delay
    print("Warp drive charged. Ready for hyperspace exploration!\n")


def main():
    """
    Main function to run the test program, which verifies the random delay microservice.
    """
    # Set up the ZeroMQ communication
    random_delay_socket = setup_zeromq()

    # Test multiple delay requests with varying ranges
    test_ranges = [
        [0.5, 2.0],
        [1.0, 3.0],
        [0.1, 1.0]
    ]

    for time_range in test_ranges:
        # Request a random delay and simulate the space exploration process
        warp_delay = request_random_delay(random_delay_socket, time_range)
        simulate_space_exploration(warp_delay)

    print("All tests completed successfully.")


if __name__ == "__main__":
    main()

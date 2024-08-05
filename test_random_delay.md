# Random Delay Microservice Test Program
## Overview
This test program verifies the functionality of the random delay microservice. It simulates interaction with the microservice using ZeroMQ sockets, requesting random delays, and simulating their effect in a space exploration scenario.

## Requirements
- Python 3.x: Required to run the test program.

- ZeroMQ (pyzmq): Used for communication between the test program and the microservice. Install using pip:
```
pip install pyzmq
```
- Random Delay Microservice: The microservice (`random_delay_microservice.py`) must be running.

## Setting Up the Microservice
#### 1 - Microservice A Script

The file named `random_delay_microservice.py` contains Microservice A's code below:
```
import zmq
import random
import time

# Create a ZeroMQ context
context = zmq.Context()

# Create a socket to reply to requests
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5558")  # Bind to a port

print("Random Delay Microservice is running...")

while True:
    # Wait for the next request from the client
    time_delay_range = socket.recv_pyobj()

    # Generate a random delay within the specified range
    random_delay = random.uniform(time_delay_range[0], time_delay_range[1])

    # Send the random delay back to the client
    socket.send_pyobj(random_delay)

    # Optionally, sleep to simulate processing time
    time.sleep(0.1)
```
#### 2 - Run the Microservice

Open a terminal and execute the script:

```
python random_delay_microservice.py
```
This will start the microservice, ready to accept requests from the test program.

## Running the Test Program
#### 1 - Test Program Code 

The file named `test_random_delay.py` with the code below, will test Microservice A expected outputs:

```
import zmq
import time

def test_random_delay_microservice():
    """
    Test program for the Random Delay Microservice.
    Simulates a space travel scenario using random warp delays.
    """

    # Create a ZeroMQ context
    context = zmq.Context()

    # Create a socket to request random delays
    random_delay_socket = context.socket(zmq.REQ)
    random_delay_socket.connect("tcp://localhost:5558")  # Connect to the microservice

    # Example time range for warp charge delay
    time_delay_range = [0.5, 2.0]

    # Send the time range to the microservice
    random_delay_socket.send_pyobj(time_delay_range)

    # Receive the random delay from the microservice
    warp_delay = random_delay_socket.recv_pyobj()
    print(f"Warp delay received: {warp_delay:.2f} seconds")

    # Simulate the delay in the exploration or travel process
    print("Charging warp drive...")
    time.sleep(warp_delay)  # Use the received delay
    print("Warp drive charged. Ready for exploration!")

if __name__ == "__main__":
    test_random_delay_microservice()
```
#### 2 - Run the Test Program

Open another terminal and execute the test program:

```
python test_random_delay.py
```
The test program will request a random delay from the microservice and simulate a warp drive charging process using the received delay.

## Expected Output
The test program will request random delays from the microservice, simulate the delay in space exploration, and print relevant messages to the console. You should see messages indicating the requested delay range, the received delay, and the simulation of the space exploration process.

When you run the test program, you should see output similar to the following:

```
Warp delay received: 1.34 seconds
Charging warp drive...
Warp drive charged. Ready for exploration!
```

## Troubleshooting
- Ensure both the microservice and test program are running simultaneously, as they need to communicate with each other.

- If you encounter connection issues, check that the port numbers match in both scripts and that there are no firewall or network issues blocking the communication.

## Additional Information
- The test program is designed to be simple and illustrative. For more complex integration, consider expanding the functionality to handle different scenarios and error conditions.

- Modify the time_delay_range in test_random_delay.py to test different delay ranges as needed.
---
## Conclusion
This test program ensures that the random delay microservice operates correctly, providing a crucial component for realistic space exploration simulations. By following these steps, you can verify the microservice's functionality and its integration with your space exploration application.
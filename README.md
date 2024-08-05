# Microservice A - Galactic Delay Generator
<!-- HTML File Switcher -->
<div style="text-align: left; font-family: Arial, sans-serif;">
  <a href="Microservice_Documentation.md" style="margin: 20px; padding: 20px 30px; background-color: #4CAF50; color: white; text-align: center; text-decoration: none; border-radius: 4px; cursor: pointer;">Microservice Doc</a>
  <a href="test_random_delay.md" style="margin: 20px; padding: 20px 30px; background-color: #4CAF50; color: white; text-align: center; text-decoration: none; border-radius: 4px; cursor: pointer;">Testing Doc</a>
</div>



## Program Description

The Random Delay Microservice is designed to generate random delays within a specified time range to simulate space travel scenarios. It is implemented using Python and communicates with the main space exploration application via ZeroMQ sockets. The microservice listens for requests from the main application, generates a random delay within the requested range, and sends this delay back to the application. This delay is then used to simulate realistic time lapses in the space travel experience.

The main components of the program include:

- **ZeroMQ Communication:** Establishes a request-reply pattern for efficient message passing between the main application and the microservice.
- **Random Delay Generation:** Utilizes Python's `random.uniform()` to generate a delay within the specified range.
- **Space Travel Simulation:** The main application uses the generated delay to simulate the charging time of a warp drive or other space travel processes, enhancing the user experience with dynamic, unpredictable delays.

The program is accompanied by a test script to verify the functionality of the microservice, ensuring that it correctly generates delays and communicates with the main application.

# Communication Contract
## Requesting Data from the Microservice:

- **Setup ZeroMQ:**

```
import zmq

# Create a ZeroMQ context
context = zmq.Context()

# Create a socket to request random delays
random_delay_socket = context.socket(zmq.REQ)
random_delay_socket.connect("tcp://localhost:5558")  # Connect to your microservice
```

- **Request a Random Delay:**

```
# Example time range for warp charge delay
time_delay_range = [0.5, 2.0]

# Send the time range to the microservice
random_delay_socket.send_pyobj(time_delay_range)

# Receive the random delay from the microservice
warp_delay = random_delay_socket.recv_pyobj()
print(f"Warp delay received: {warp_delay:.2f} seconds")
```

## Receiving Data from the Microservice:

- **Use the Delay in the Application:**

```
import time

# Simulate the delay in the exploration or travel process
print("Charging warp drive...")
time.sleep(warp_delay)  # Use the received delay
print("Warp drive charged. Ready for exploration!")
```

## UML Sequence Diagram

The UML sequence diagram below shows the request and response process between the main application and the microservice.
```
+------------------------------------------------------+
|              Space Travel Application                |
+------------------------------------------------------+
|   +-----------------+     +---------------------+    |
|   |   Main Program  |     |  Microservice A     |    |
|   +-----------------+     +---------------------+    |
|          |                            |              |
|          |     Send request with      |              |
|          |   time range [0.5, 2.0]    |              |
|          |--------------------------->|              |
|          |                            |              |
|          |                            |              |
|          |                            |   Generate   |
|          |                            |  random delay|
|          |                            |              |
|          |                            |    within    |
|          |                            |   specified  |
|          |                            |    range     |
|          |                            |              |
|          |                            |              |
|          |   Receive random delay     |              |
|          |<---------------------------|              |
|          |                            |              |
|          |                            |              |
|          | Simulate delay using       |              |
|          | received delay             |              |
|          | (e.g.,                     |              |
|          | time.sleep(warp_delay))    |              |
|          |                            |              |
+------------------------------------------------------+
```
## UML Sequence Explanation:

### Space Travel Application:

- **Main Program:** Represents the main application that sends and receives requests from the microservice.
- **Microservice A:** Represents the random delay generator.

### Steps:

1. **Send Request:**
   - The main program sends a request with a specified time range (e.g., `[0.5, 2.0]`) to the microservice.

2. **Generate Random Delay:**
   - The microservice generates a random delay within the specified range.

3. **Receive Delay:**
   - The main program receives the generated random delay.

4. **Simulate Delay:**
   - The main program uses the received delay to simulate a delay in space exploration (e.g., `time.sleep(warp_delay)`).

This sequence diagram textually represents how the main application interacts with the microservice, highlighting the communication flow and actions taken by both parties.

1. **Main Application:** Sends a time range to the microservice using ZeroMQ.
2. **Microservice:** Receives the time range, generates a random delay, and sends it back.
3. **Main Application:** Receives the random delay and uses it in the application flow.

## Mitigation Plan
**For which teammate did you implement “Microservice A”?**
- The microservice was implemented for `Bradley Sommer`'s space travel application.

**What is the current status of the microservice?**
- The microservice is `fully implemented and operational`.

**If the microservice isn’t done, which parts aren’t done and when will they be done?**
- N/A, Microservice is `done` and fully working

**How is your teammate going to access your microservice?**
- The microservice code is `available on GitHub`. My teammate should clone the repository and run the microservice `locally`.

**If your teammate cannot access/call YOUR microservice, what should they do?**
- If there are any access issues, they should contact me immediately. I am available to help resolve any issues from `6 PM to - 9 PM PST`.

** If your teammate cannot access/call your microservice, by when do they need to tell you?**
- They should inform me of any issues `within 24 hours` of attempting to access the microservice.

**Is there anything else your teammate needs to know?**
- Ensure that both the microservice and test program are running on the same network and that `port 5558` is open for communication. Let me know if there are any firewall restrictions.

## Additional Documentation

The repository includes two additional documentation files that provide detailed information about the microservice and the test program:

1. **[Microservice Documentation (`Microservice_Documentation.md`)](./Microservice_Documentation.md):**
   - This document outlines the implementation details of the random delay microservice, including setup instructions, code explanations, and communication protocols.

2. **[Test Program Documentation (`Test_Random_Delay.md`)](./Test_Random_Delay.md):**
   - This document provides a comprehensive guide for setting up and running the test program to verify the functionality of the microservice. It includes code samples, expected outputs, and troubleshooting tips.

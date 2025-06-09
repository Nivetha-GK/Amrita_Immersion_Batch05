## 📅 Day 2 Summary – Simulation & Sensor Data Streaming

Simulating the core functionality of the Smart AGV Navigation system within a virtual environment, followed by the successful integration of cloud-based data streaming for remote monitoring and logging purposes.

🔧 1. Virtual Simulation using Wokwi
To simulate the hardware setup without requiring physical components, the Wokwi online simulator was employed. This platform allowed for realistic emulation of embedded systems based on the Raspberry Pi Pico W board.

Virtual hardware setup included:

Raspberry Pi Pico W as the central processing unit

Ultrasonic Sensor (HC-SR04) for detecting obstacles

Infrared (IR) Sensor for line detection or edge tracking

PIR Sensor for motion/human presence detection

The simulator environment enabled interactive testing of input/output behavior in response to various sensor readings.

💻 2. Sensor Integration & Programming
The Raspberry Pi Pico W was programmed using MicroPython, enabling it to interface with all three sensors. The code included:

Triggering and reading distance from the Ultrasonic sensor

Reading digital signals from IR and PIR sensors

Handling GPIO pin configuration for input/output operations

Processing and packaging sensor data for transmission

Real-time sensor values were printed in the simulation terminal for initial debugging and verification.

🌐 3. Establishing Wi-Fi Connectivity
An essential objective of the day was to enable wireless communication between the AGV system and the cloud:

The Pico W was configured to connect to a local Wi-Fi network (in Wokwi simulation, a virtual network was emulated).

Successful IP address allocation confirmed a stable connection.

☁️ 4. Data Streaming to ThingSpeak
The next milestone involved setting up a ThingSpeak cloud channel for data logging and visualization.

Using the ThingSpeak Write API Key, sensor readings were transmitted via HTTP POST requests.

Data fields were mapped as:

Field 1 – Ultrasonic Sensor distance

Field 2 – IR Sensor output

Field 3 – PIR Sensor output

The data was successfully visualized as real-time plots and logs on the ThingSpeak dashboard.

⏱ 5. Timing Control and Compliance
To comply with ThingSpeak’s data rate limit (minimum 15 seconds between updates), a time.sleep(15) delay was implemented in the program.

This ensured smooth, uninterrupted streaming without exceeding server limits.

Timestamped entries were automatically recorded by ThingSpeak for future analysis.

✅ Outcome
A fully functional virtual simulation of the AGV navigation system was developed.

Sensor readings were successfully captured and streamed live to the ThingSpeak cloud.

Real-time cloud visualization confirmed the system’s readiness for physical hardware implementation and further enhancements such as machine learning or predictive maintenance.

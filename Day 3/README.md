# 🚗 Smart AGV Navigation with Sensor & Cloud Integration

This project implements a Smart Automated Guided Vehicle (AGV) system using Raspberry Pi Pico W and multiple sensors. The AGV detects obstacles and environmental changes, streams live data to the cloud, and enables predictive analytics via ThingSpeak.

---

## 🔧 Features

- Integration of **Ultrasonic**, **IR**, and **PIR** sensors with **Raspberry Pi Pico W**
- Real-time sensor data acquisition and processing
- **Wi-Fi communication** and **ThingSpeak cloud streaming**
- Obstacle detection and motion tracking simulation
- Downloadable CSV logs for further analysis

---

## 🧰 Technologies Used

- Raspberry Pi Pico W (MicroPython)
- Ultrasonic, IR, and PIR sensors
- Wokwi Simulator (for virtual prototyping)
- ThingSpeak IoT Cloud Platform
- Python & HTTP for API communication

---

## 🚀 Workflow

1. Sensors detect environment (distance, motion, line/surface).
2. Raspberry Pi Pico W collects and formats data.
3. Data is sent to **ThingSpeak**.
4. Live plots and logs are displayed on the ThingSpeak dashboard.
5. CSV datasets can be exported for ML applications.

---

import time
from machine import Pin, time_pulse_us

# ===== Sensor Pins =====
TRIG = Pin(2, Pin.OUT)
ECHO = Pin(3, Pin.IN)
PIR = Pin(4, Pin.IN)
IR = Pin(5, Pin.IN)

# ===== Function to measure distance =====
def measure_distance():
    TRIG.low()
    time.sleep_us(2)
    TRIG.high()
    time.sleep_us(10)
    TRIG.low()
    duration = time_pulse_us(ECHO, 1, 30000)  # Timeout 30ms
    distance_cm = (duration / 2) / 29.1 if duration > 0 else -1
    return distance_cm

# ===== Main Loop =====
while True:
    distance = measure_distance()
    pir_value = PIR.value()
    ir_value = IR.value()

    print(f"Distance: {distance:.2f} cm, PIR: {pir_value}, IR: {ir_value}")
    time.sleep(1)

import network
import urequests
import time
from machine import Pin, time_pulse_us

# ===== Wi-Fi Credentials =====
SSID = 'Wokwi-GUEST'
PASSWORD =''

# ===== ThingSpeak API Key =====
API_KEY = 'XP4UFTNGLWRTMIRW'

# ===== Sensor Pins =====
TRIG = Pin(2, Pin.OUT)
ECHO = Pin(3, Pin.IN)
PIR = Pin(4, Pin.IN)
IR = Pin(5, Pin.IN)
BUZZER = Pin(6, Pin.OUT)

# ===== Connect to Wi-Fi =====
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)
print("Connecting to Wi-Fi", end="")
while not wlan.isconnected():  
    print(".", end="")
    time.sleep(0.5)
print("\nConnected to Wi-Fi")

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

    # ===== Buzzer Alert Condition =====
    if distance < 38 and pir_value == 1 and ir_value == 1:
        BUZZER.on()
        print("⚠️ ALERT: Buzzer ON")
    else:
        BUZZER.off()

    # ===== Send to ThingSpeak =====
    url = f"https://api.thingspeak.com/update?api_key={API_KEY}&field1={distance:.2f}&field2={pir_value}&field3={ir_value}"

    try:
        response = urequests.get(url)
        print("Data sent to ThingSpeak:", response.text)
        response.close()
    except Exception as e:
        print("Failed to send data:", e)

    time.sleep(2)


import dht
import time
import network
import urequests
from machine import Pin
sensor = dht.DHT22(Pin(15))
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect("Wokwi-GUEST", "")
print("Connecting to Wi-Fi...")
while not wifi.isconnected():
    time.sleep(1)
print("Wi-Fi connected!")
API_KEY = "YOUR_WRITE_API_KEY"
while True:
    sensor.measure()
    temperature = sensor.temperature()
    humidity = sensor.humidity()
    print("Temperature:", temperature, "C")
    print("Humidity:", humidity, "%")
    url = "https://api.thingspeak.com/update?api_key=" + API_KEY
    url = url + "&field1=" + str(temperature)
    url = url + "&field2=" + str(humidity)
    response = urequests.get(url)
    print("ThingSpeak response:", response.text)
    time.sleep(15)

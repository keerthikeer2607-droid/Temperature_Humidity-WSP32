ESP32 Temperature and Humidity Monitoring

1. Project Title

EnviroTrack: IoT-Based Temperature and Humidity Monitoring Using ESP32 and DHT22

2. Problem Statement

Monitoring temperature and humidity is useful in many environments. This project uses an ESP32 and DHT22 sensor to measure temperature and humidity and sends the collected data to the ThingSpeak cloud platform for monitoring through graphs.

3. Objectives
- To measure temperature and humidity using the DHT22 sensor.
- To use ESP32 for collecting sensor data.
- To send sensor data to the ThingSpeak cloud platform using Wi-Fi.
- To display temperature and humidity readings using graphs.
- To understand the basic working of an IoT monitoring system.

4. Components and Software Used-
Hardware:
- ESP32
- DHT22 Temperature and Humidity Sensor
Software and Platforms:
- Wokwi
- MicroPython
- ThingSpeak
- GitHub
  
5. Circuit Diagram
The DHT22 sensor is connected to the ESP32 as follows:
- DHT22 VCC → ESP32 3V3
- DHT22 DATA → ESP32 GPIO 15
- DHT22 GND → ESP32 GND
  
Circuit diagram: "circuit_diagram.png"

6. Working Principle
The DHT22 sensor measures temperature and humidity from the surrounding environment. The ESP32 reads these values through GPIO 15. The ESP32 connects to Wi-Fi and sends the sensor readings to the ThingSpeak cloud platform. Temperature is stored in Field 1 and humidity is stored in Field 2. ThingSpeak displays the received data using graphs.

7. Program Explanation
The program uses the DHT22 sensor library to read temperature and humidity values.
The ESP32 connects to the Wokwi Wi-Fi network. After connecting to Wi-Fi, the program reads the temperature and humidity from the DHT22 sensor.
The values are sent to ThingSpeak using the ThingSpeak Write API Key. The program repeats the process after a delay.

8. Output
The Wokwi Serial Monitor displays the temperature, humidity and ThingSpeak response.

ThingSpeak displays:
- Field 1 → Temperature
- Field 2 → Humidity
  
Output screenshot: "wokwi_output.png"

ThingSpeak graph: "thingspeak_output.png"

9. Applications
- Environmental monitoring
- Smart home systems
- Weather monitoring
- Greenhouse monitoring
- IoT-based temperature and humidity monitoring

10. Limitations
- The system depends on Wi-Fi connectivity for sending data to ThingSpeak.
- The project is implemented as a Wokwi simulation.
- Sensor readings may vary depending on the sensor and environment.

11. Future Scope
- Add more sensors.
- Use a real ESP32 and DHT22 hardware setup.
- Add alerts when temperature or humidity crosses a limit.
- Develop a mobile or web dashboard for monitoring.
- Store and analyze sensor data for longer periods.

12. Team Members' Details
Name: Keerthi A
Register Number: U03ZW24S0097
Team Members:
Sreethan , Jewel Mary Jibi

13. Wokwi Project Link
https://wokwi.com/projects/475682178620641281

14. ThingSpeak Channel Link
https://thingspeak.mathworks.com/channels/3500612/private_show

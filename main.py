import time
from w1thermsensor import W1ThermSensor

# Initialize the sensor
sensor = W1ThermSensor()

while True:
    # Read the temperature
    temperature_celsius = sensor.get_temperature()
    temperature_fahrenheit = sensor.get_temperature(W1ThermSensor.DEGREES_F)
    
    # Print the temperature
    print(f"Temperature: {temperature_celsius:.2f}°C / {temperature_fahrenheit:.2f}°F")
    
    # Wait for a second before reading again
    time.sleep(1)

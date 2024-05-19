import time
from urllib import request
from w1thermsensor import W1ThermSensor

# Initialize the sensor
sensor = W1ThermSensor()

while True:
    # Read the temperature
    temperature_celsius = sensor.get_temperature()
    #temperature_fahrenheit = sensor.get_temperature(W1ThermSensor.DEGREES_F)
    
    # Print the temperature
    print(f"Temperature: {temperature_celsius:.2f}°C")


    form_url = "https://docs.google.com/forms/d/e/1FAIpQLSck0PwBvp_kwBuYo6aXPpm7bR8SmiCUmsrreE6DkoVRF32N6w/formResponse?usp=pp_url&entry.1936681108={}&submit=Submit".format(temperature_celsius)
  
  
    request.urlopen(form_url)
    
    # Wait for a second before reading again
    time.sleep(1)


#   https://docs.google.com/spreadsheets/d/1rZtET8V9EjBPN9CqarLRkBieTXYhDZyPql7ZwbCThN8/edit?usp=sharing

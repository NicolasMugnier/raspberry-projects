import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT22
pin = 2

try:
    while True:
    
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)


        if humidity is not None and temperature is not None:
            print(f"Temperature: {temperature:.1f} °C, Humidity: {humidity:.1f} %")
        else:
            print("Failed to retrieve data from the DHT22 sensor.")

        time.sleep(2)

except KeyboardInterrupt:
    print("\nExiting...")

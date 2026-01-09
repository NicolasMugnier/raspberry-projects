from flask import Flask, render_template
import Adafruit_DHT
import json

app = Flask(__name__)

sensor = Adafruit_DHT.DHT22
pin = 2

@app.route('/')
def index():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return render_template('index.html', temperature='{:04.1f}'.format(temperature), humidity='{:05.2f}'.format(humidity))

@app.route('/data')
def data():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    humidity = '{:04.1f}'.format(humidity)
    temperature = '{:05.2f}'.format(temperature)
    return json.dumps({"temperature":{"value":temperature, "unit":"°C"}, "humidity":{"value":humidity, "unit":"%"}})


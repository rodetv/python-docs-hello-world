from flask import Flask
import paho.mqtt.client as mqtt
app = Flask(__name__)

@app.route("/")
def hello():
    return "YOLO"
    return "Hello, World!"
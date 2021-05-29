from flask import Flask
import paho.mqtt.client as mqtt
app = Flask(__name__)

@app.route("/")

# Function to process recieved message
def process_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)



# Create client
client = mqtt.Client(client_id="subscriber-1")

# Assign callback function
client.on_message = process_message

# Connect to broker
client.connect(test.mosquitto.org,1883,60)

# Subscriber to topic
client.subscribe("#")

# Run loop
client.loop_forever()
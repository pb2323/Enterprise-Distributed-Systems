import paho.mqtt.client as mqtt

# Global counter for received messages
received_counter = 0

# Define the callback function for when a message is received
def on_message(client, userdata, msg):
    global received_counter
    received_counter += 1
    if received_counter % 1000 == 0:
        print(f"Messages received: {received_counter}")

# Define the callback function for when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("test/topic", qos=1)  # Using QoS 1 for at least once delivery

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print(f"Unexpected disconnection: {rc}")

# Create a client instance
client = mqtt.Client()

# Assign the callback functions
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

# Connect to the broker
broker = "127.0.0.1"
port = 1883

try:
    client.connect(broker, port, 60)
except Exception as e:
    print(f"Failed to connect to broker: {e}")
    exit(1)

try:
    print("Subscriber started. Press Ctrl+C to stop...")
    client.loop_forever()
except KeyboardInterrupt:
    print("\nSubscriber stopped by user")
    print(f"Total messages received: {received_counter}")
    client.disconnect()
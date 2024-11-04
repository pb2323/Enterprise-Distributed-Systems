import paho.mqtt.client as mqtt
import time

# Define the callback function for when a message is published
def on_publish(client, userdata, mid, properties=None):
    global publish_counter
    publish_counter += 1
    if publish_counter % 1000 == 0:
        print(f"Messages published: {publish_counter}")

# Create a client instance
client = mqtt.Client()
publish_counter = 0

# Assign the callback function
client.on_publish = on_publish

# Connect to the broker
broker = "127.0.0.1"
port = 1883

try:
    client.connect(broker, port, 60)
except Exception as e:
    print(f"Failed to connect to broker: {e}")
    exit(1)

# Start the loop to process callbacks
client.loop_start()

topic = "test/topic"
TOTAL_MESSAGES = 1000000

try:
    for i in range(TOTAL_MESSAGES):
        msg = f"Message #{i+1} from IoT Sensor"
        info = client.publish(
            topic,
            payload=msg.encode('utf-8'),
            qos=1,  # Using QoS 1 for at least once delivery
        )
        info.wait_for_publish()
        
        # Optional: Add a small delay to prevent overwhelming the broker
        if i % 1000 == 0:
            time.sleep(0.1)

except KeyboardInterrupt:
    print("\nPublisher stopped by user")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print(f"\nTotal messages published: {publish_counter}")
    client.loop_stop()
    client.disconnect()
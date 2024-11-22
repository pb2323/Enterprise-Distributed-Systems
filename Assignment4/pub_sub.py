import paho.mqtt.client as mqtt
import pandas as pd
import json
import time

# MQTT broker settings
BROKER_ADDRESS = "broker.hivemq.com"  # Using HiveMQ's public broker
PORT = 1883  # Standard MQTT port

# MQTT topics mapped to each reservoir
TOPICS = {
    "shasta": "SHASTA/WML",
    "oroville": "OROVILLE/WML",
    "sonoma": "SONOMA/WML"
}

# Global dictionary to store aggregated data
daily_aggregates = {}


def initialize_client():
    """
    Initialize the MQTT client and set up callbacks.
    """
    client = mqtt.Client(protocol=mqtt.MQTTv5)
    client.on_connect = handle_connect
    client.on_message = handle_message
    return client


def handle_connect(client, userdata, flags, rc, properties=None):
    """
    Callback for handling MQTT connection.
    """
    if rc == 0:
        print("Connected successfully.")
        subscribe_to_topics(client)
    else:
        print(f"Connection failed with code {rc}: {mqtt.connack_string(rc)}")


def subscribe_to_topics(client):
    """
    Subscribe to all reservoir topics.
    """
    for topic in TOPICS.values():
        client.subscribe(topic)


def handle_message(client, userdata, msg):
    """
    Callback for processing received MQTT messages.
    """
    process_message(msg)


def process_message(msg):
    """
    Decode and aggregate message data.
    """
    try:
        data = json.loads(msg.payload.decode())
        update_aggregates(data, msg.topic)
    except Exception as e:
        print(f"Error processing message: {e}")


def update_aggregates(data, topic):
    """
    Update the daily aggregates with new data.
    """
    date = data['Date']
    taf = data['TAF']
    reservoir = topic.split('/')[0].lower()

    if date not in daily_aggregates:
        daily_aggregates[date] = {}
    if reservoir not in daily_aggregates[date]:
        daily_aggregates[date][reservoir] = []

    daily_aggregates[date][reservoir].append(taf)
    print_daily_summary(date)


def print_daily_summary(date):
    """
    Print the aggregated data for a specific date.
    """
    if date in daily_aggregates:
        for reservoir, values in daily_aggregates[date].items():
            average_taf = sum(values) / len(values)
            print(f"Date: {date}, Reservoir: {reservoir}, Average TAF: {average_taf}")


def load_csv_to_json(filepath):
    """
    Load data from a CSV file and convert it to JSON format.
    """
    df = pd.read_csv(filepath)
    return df.to_dict(orient='records')


def publish_data(client, data, topic):
    """
    Publish data to a specific MQTT topic.
    """
    for entry in data:
        message = json.dumps(entry)
        client.publish(topic, message)
        time.sleep(1)  # Simulate time delay between messages


def main():
    """
    Main function to initialize client, process data, and publish messages.
    """
    client = initialize_client()

    try:
        client.connect(BROKER_ADDRESS, PORT, 60)
    except Exception as e:
        print(f"Failed to connect to MQTT broker: {e}")
        return

    client.loop_start()

    try:
        shasta_data = load_csv_to_json("./Shasta_WML(Sample).csv")
        oroville_data = load_csv_to_json("./Oroville_WML(Sample).csv")
        sonoma_data = load_csv_to_json("./Sonoma_WML(Sample).csv")

        publish_data(client, shasta_data, TOPICS["shasta"])
        publish_data(client, oroville_data, TOPICS["oroville"])
        publish_data(client, sonoma_data, TOPICS["sonoma"])
    except Exception as e:
        print(f"Error processing files: {e}")
    finally:
        time.sleep(20)  # Adjust based on your need
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()

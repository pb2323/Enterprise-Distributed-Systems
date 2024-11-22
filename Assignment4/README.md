# California Reservoirs MQTT Data Aggregator

## Project Overview
This project highlights the application of MQTT to monitor and aggregate Water Mark Levels (TAF) from various California reservoirs. It focuses on handling and processing real-time data, subscribing to specific MQTT topics for each reservoir, and computing daily average TAF values to support effective water resource management.

## Features
- **Real-Time Data Collection:** Leverages the MQTT protocol to gather TAF data from multiple reservoirs in real-time.
- **Daily Aggregation:** Processes collected data to calculate daily average water mark levels.
- **Report Generation:** Produces detailed summaries of aggregated data, aiding in trend analysis and strategic water resource planning.

## Technology Stack
- **MQTT:** Facilitates message-based communication and data transmission.
- **Python:** Primary programming language for developing subscriber and publisher functionalities.
- **Paho-MQTT:** Python library used for connecting with and interacting with MQTT brokers.

## Getting Started

### Prerequisites
- Python 3.8 or newer
- Paho-MQTT Python library

### Installation
Install the required library using the following command:

```bash
pip install paho-mqtt

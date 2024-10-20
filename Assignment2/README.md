# WebSocket Real-Time Communication Project

This project demonstrates a real-time, bidirectional communication system using WebSockets. It consists of a Python server and an HTML/JavaScript client that exchange messages, with the server modifying each received message before sending it back.

Project Documentation - [https://docs.google.com/document/d/1ovz4xncT1jcaYbQASFPkpvz9tmNFk3BCpAhB_8CpYz4/edit?usp=sharing](https://docs.google.com/document/d/1ovz4xncT1jcaYbQASFPkpvz9tmNFk3BCpAhB_8CpYz4/edit?usp=sharing)

## Features

- Full-duplex WebSocket communication
- Python-based WebSocket server using `asyncio` and `websockets`
- Browser-based client with a user-friendly interface
- Ability to send single messages or multiple messages in rapid succession
- Server-side message modification (appending random numbers)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:

2. Install the required Python packages:
   ```
   pip3 install -r requirements.txt
   ```

## Usage

1. Start the WebSocket server:
   ```
   python server.py
   ```
   The server will start running on `ws://localhost:8765`.

2. Open `client.html` in a web browser.

3. Use the client interface to interact with the WebSocket server:
   - Enter a custom message or use the default message
   - Click "Send One Message" to send a single message
   - Click "Start 10,000 Messages" to send multiple messages in rapid succession

4. Observe the sent and received messages in the client interface.

## Project Structure

- `websocketserver.py`: The Python WebSocket server
- `websocketclient.py`: The Python WebSocket client
- `client.html`: The HTML/JavaScript client
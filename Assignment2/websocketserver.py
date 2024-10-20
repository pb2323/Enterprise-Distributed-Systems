import asyncio
import websockets
import random

async def handle_client(websocket):
    try:
        async for message in websocket:
            # Append a random number to the client message
            random_number = random.randint(1, 1000)
            modified_message = f"{message} - {random_number}"
            
            # Send the modified message back to the client
            await websocket.send(modified_message)
    except websockets.exceptions.ConnectionClosedOK:
        pass

async def main():
    server = await websockets.serve(handle_client, "localhost", 8765)
    print("WebSocket server started on ws://localhost:8765")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
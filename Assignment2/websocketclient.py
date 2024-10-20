import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    
    async with websockets.connect(uri) as websocket:
        for i in range(10000):
            message = f"Hello Server {i}"
            await websocket.send(message)
            
            response = await websocket.recv()
            print(f"Received: {response}")

if __name__ == "_main_":
    asyncio.run(hello())
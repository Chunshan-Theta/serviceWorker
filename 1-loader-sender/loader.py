import asyncio
import json
import socketio

# standard Python
sio = socketio.SimpleClient()





# The main function that will handle connection and communication
# with the server
async def ws_client():
    print("WebSocket: Client Connected.")
    # Connect to the server
    async with socketio.AsyncSimpleClient() as sio:
        await sio.connect("ws://127.0.0.1:8000")

        while True:
            print(f'[Ongoing]  Getting body to server...')
            event = await sio.receive()
            print(f'[Success]  Get body from server: "{event[0]}" with arguments {event[1:]}')
            try:
                response = json.loads(event[1])
                print(f"[Success] Paser body to server.{response}")
            except json.decoder.JSONDecodeError:
                print(f"[WARN] Paser body to server.{event[1]}")
            

 
# Start the connection
asyncio.run(ws_client())
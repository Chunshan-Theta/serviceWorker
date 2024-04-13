import asyncio
import json
import socketio

# standard Python
with socketio.SimpleClient() as sio:
    sio.connect("ws://127.0.0.1:8000")
    body = {
        "userId": "00001",
        "action": "test",
        "log": "200 GET \"something text\" 中文測試"
    }
    print(f"[OnGoing] Sending body to server: {body}")
    sio.emit("toLoader",json.dumps(body))
    print(f"[Success] Send body to server.")

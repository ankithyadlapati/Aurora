from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import Dict, List


router = APIRouter()


# Very small collaborative hub: room_id -> set of websockets
rooms: Dict[str, List[WebSocket]] = {}


@router.websocket('/{room_id}')
async def ws_endpoint(websocket: WebSocket, room_id: str):
await websocket.accept()
rooms.setdefault(room_id, []).append(websocket)
try:
while True:
data = await websocket.receive_json()
# naive broadcast — replace with OT/CRDT logic in production
for ws in rooms[room_id]:
if ws != websocket:
await ws.send_json(data)
except WebSocketDisconnect:
rooms[room_id].remove(websocket)

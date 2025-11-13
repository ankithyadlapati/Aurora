export function initSocket(roomId){
const ws = new WebSocket(`ws://${location.hostname}:8000/ws/${roomId}`)
ws.onopen = ()=> console.log('ws open')
return ws
}

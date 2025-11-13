import React, {useEffect, useState, useRef} from 'react'
import {initSocket} from '../ws'


export default function Editor(){
const [content, setContent] = useState('')
const socketRef = useRef(null)


useEffect(()=>{
socketRef.current = initSocket('room-demo')
socketRef.current.onmessage = (ev)=>{
const msg = JSON.parse(ev.data)
if(msg.type === 'code_update') setContent(msg.payload)
}
return ()=> socketRef.current.close()
},[])


function onChange(e){
setContent(e.target.value)
socketRef.current.send(JSON.stringify({type:'code_update', payload:e.target.value}))
}


return <textarea value={content} onChange={onChange} className="w-full h-[70vh] p-2" />
}

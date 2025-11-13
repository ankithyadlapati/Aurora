import React from 'react'
import Editor from './components/Editor'
import Dashboard from './components/Dashboard'


export default function App(){
return (
<div className="min-h-screen p-6">
<h1 className="text-2xl font-bold mb-4">Aurora Interview Platform</h1>
<div className="grid grid-cols-2 gap-4">
<Editor />
<Dashboard />
</div>
</div>
)
}

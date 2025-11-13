from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter()


class LoginIn(BaseModel):
username: str
password: str


# NOTE: stubbed authentication for demo
@router.post('/login')
async def login(payload: LoginIn):
if payload.username == 'interviewer' and payload.password == 'hunter2':
return {"token": "demo-token", "role": "interviewer"}
raise HTTPException(status_code=401, detail='Invalid')

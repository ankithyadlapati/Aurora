from fastapi import FastAPI
from .websocket import router as ws_router
from .problems import router as problems_router
from .auth import router as auth_router


app = FastAPI(title="Aurora Interview Platform")


app.include_router(auth_router, prefix="/auth")
app.include_router(problems_router, prefix="/api/problems")
app.include_router(ws_router, prefix="/ws")


@app.get("/health")
async def health():
return {"status": "ok"}

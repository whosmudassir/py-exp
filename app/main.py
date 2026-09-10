from fastapi import FastAPI, WebSocket
from app.routes.users import router as user_router
from app.middleware.timer import time_middleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() 

app.middleware("http")(time_middleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
                   )

@app.get('/')
def index():
    return {"Hello from server!"}


app.include_router(user_router)
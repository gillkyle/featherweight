import subprocess

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UserResponse(BaseModel):
    user_id: str
    email: str
    name: str


@app.get("/")
async def root():
    return {"message": "Hello world. Welcome to FastAPI!"}


@app.get("/user", response_model=UserResponse)
async def current_user():
    return {
        "user_id": "0123456789",
        "email": "me@kylegill.com",
        "name": "Kyle Gill",
    }


def dev():
    try:
        subprocess.check_output(["redis-cli", "ping"], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError:
        print("Redis is not already running, have you started it with redis-server?")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

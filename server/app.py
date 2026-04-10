from fastapi import FastAPI
from pydantic import BaseModel
from env.environment import BugEnv

app = FastAPI()
env = BugEnv()

class Action(BaseModel):
    action: str

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: Action):
    result = env.step(action.action)
    return result
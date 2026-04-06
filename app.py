from fastapi import FastAPI
from environment import StudyEnv
from models import ActionInput

app = FastAPI()
env = StudyEnv()

@app.get("/")
def home():
    return {"message": "AI Study Planner Environment Running"}

@app.get("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(input: ActionInput):
    state, reward, done = env.step(input.action)
    return {
        "state": state,
        "reward": reward,
        "done": done
    }

@app.get("/tasks")
def tasks():
    return {
        "tasks": ["easy", "medium", "hard"]
    }

@app.get("/grader")
def grader():
    score = max(0, 1 - env.state["syllabus_left"]/100)
    return {"score": score}

@app.get("/baseline")
def baseline():
    return {"action": "study"}

import random

class StudyEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.state = {
            "hours_available": 5,
            "syllabus_left": 100,
            "energy": 10
        }
        return self.state

    def step(self, action):
        reward = 0

        if action == "study":
            self.state["syllabus_left"] -= 10
            self.state["energy"] -= 2
            reward += 5

        elif action == "rest":
            self.state["energy"] += 3
            reward += 1

        # penalties
        if self.state["energy"] <= 0:
            reward -= 5

        done = self.state["syllabus_left"] <= 0

        return self.state, reward, done

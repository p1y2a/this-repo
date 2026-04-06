from pydantic import BaseModel

class ActionInput(BaseModel):
    action: str

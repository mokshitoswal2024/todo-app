from typing import Optional
from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    title: str
    description: Optional[str]=None
    completed: bool = False

class UpdateTodo(BaseModel):
    id: Optional[int]=None
    title: Optional[str]=None
    description: Optional[str]=None
    completed: Optional[bool]=None

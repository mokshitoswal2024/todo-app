from fastapi import FastAPI, HTTPException
from typing import List
from models import Todo, UpdateTodo

app = FastAPI()

todos = []

# 4 main methods in fastapi
# GET - get some information
# POST - post some new information
# PUT - update information
# DELETE - delete something

@app.get("/todos", response_model=List[Todo])
def get_todos():
    return todos

@app.post("/todos", response_model=Todo)
def create_todo(todo: Todo):
    for existing_todo in todos:
        if todo.id == existing_todo.id:
            raise HTTPException(status_code=400, detail="Todo already exists")
    todos.append(todo)
    return todo

@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: UpdateTodo):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[i] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}", response_model=Todo)
def delete_todo(todo_id:int):
    for i, todo in enumerate(todos):
        if todo_id == todo.id:
            deleted_todo = todos.pop(i)
            return deleted_todo
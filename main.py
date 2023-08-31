
from fastapi import FastAPI, Path

app = FastAPI()
@app.get("/todos")
def get_todos(db):
    todos = []
    cursor = db.cursor()
    cursor.execute("SELECT * FROM todos")
    for row in cursor:
        todo = {
            "id": row[0],
            "task": row[1],
            "completed": row[2],
        }
        todos.append(todo)
    return todos

from fastapi import FastAPI, Path

app = FastAPI()
students = {
    1: {
        "name" : "John",
        "age": 17,
        "class": "Year 12"
    }
}

@ app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description= "The ID of the students you want to view")):
    return students[student_id]
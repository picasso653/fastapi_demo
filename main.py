
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
def get_student(student_id: int = Path(None,
 description= "The ID fo the student you want to view")):
    return students[student_id]


@app.get("/get-by-name")
def get_student(name: str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
        return {"Data": "Not Found"}
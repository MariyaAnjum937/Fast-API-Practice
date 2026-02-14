from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict
app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    branch: str
    model_config = ConfigDict(extra="forbid")
students = []
@app.post("/students")
def add_student(student: Student):
    students.append(student)
    return {"message":"student added successfully!"}

@app.get("/students")
def get_students():
    return students

@app.get("/students/{name}")
def get_student_by_name(name:str):
    for student in students:
        if student.name==name:
            return "student already exist"
    return students
@app.get("/students/{branch}")
def get_student_by_branch(branch: str):
    match_bra = []
    for student in students:
        if student.branch==branch:
            match_bra.append(student)
    return match_bra

@app.get("/students/total")
def total_students():
    return len(students)

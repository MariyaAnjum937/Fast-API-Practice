from fastapi import FastAPI
from pydantic import BaseModel, Field
app = FastAPI()


class Student(BaseModel):
    name: str
    age: int = Field(..., ge=18)
    course: str

students = {}
@app.post("/students/{student_id}")
def create_student(student_id:int, student:Student):
    students[student_id] = student
    return {
        "message":"student inserted successfully!",
        "student_id": student_id,
        "data": student
    }

@app.get("/info")
def get_student():
    return students

@app.get("/students")
def filter_students(course: str = None, min_age: int = 18):
    results = []

    for student in students.values():
        if (course is None or student.course == course) and student.age >= min_age:
            results.append(student)

    return results


    
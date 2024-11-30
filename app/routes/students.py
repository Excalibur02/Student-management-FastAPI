from fastapi import APIRouter, Query, HTTPException
from app.services.student_services import (
    create_student,
    list_students,
    get_student_by_id,
    update_student,
    delete_student,
)

router = APIRouter()

@router.post("/students", status_code=201)
async def create_student_endpoint(student: dict):
    id = create_student(student)
    return {"id": id}

@router.get("/students")
async def list_students_endpoint(country: str = None, age: int = None):
    filters = {}
    if country:
        filters["address.country"] = country
    if age:
        filters["age"] = {"$gte": age}

    all_students = list_students(filters)
    return {"data": [{"name" : students['name'],"age":students['age']} for students in all_students] }

@router.get("/students/{id}")
async def get_student_endpoint(id: str):
    return get_student_by_id(id)

@router.patch("/students/{id}", status_code=204)
async def update_student_endpoint(id: str, student: dict):
    update_student(id, student)
    return {}

@router.delete("/students/{id}", status_code=200)
async def delete_student_endpoint(id: str):
    delete_student(id)
    return {}

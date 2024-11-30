from config.database import students_collection, id_collection
from pymongo.errors import DuplicateKeyError
from fastapi import HTTPException
from app.models import student_helper

def get_next_roll_number():
    counter = id_collection.find_one_and_update(
        {"_id": "id"},
        {"$inc": {"value": 1}},
        return_document=True
    )
    return str(counter["value"])

def create_student(data: dict):
    id = get_next_roll_number()
    data["id"] = id
    try:
        students_collection.insert_one(data)
    except DuplicateKeyError:
        raise HTTPException(status_code=400, detail="ID already exists")
    return id

def list_students(filters: dict = {}):
    students = students_collection.find(filters)
    return [student_helper(student) for student in students]

def get_student_by_id(id: str):
    student = students_collection.find_one({"id": id})
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student_helper(student)

def update_student(id: str, data: dict):
    result = students_collection.update_one({"id": id}, {"$set": data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")

def delete_student(id: str):
    result = students_collection.delete_one({"id": id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")

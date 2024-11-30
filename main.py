from fastapi import FastAPI
from app.routes.students import router as student_router

app = FastAPI(title="Student Management System", version="1.0.0")

# Routing
app.include_router(student_router)

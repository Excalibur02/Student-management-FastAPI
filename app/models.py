def student_helper(student) -> dict:
    return {
        "name": student["name"],
        "age": student["age"],
        "address": {
            "city": student["address"]["city"],
            "country": student["address"]["country"],
        },
    }

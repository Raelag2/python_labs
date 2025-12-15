from models import Student
from pathlib import Path
from typing import List
import json

def student_to_json(students, path):
    students_dict = []
    for student in students:
        student_dict = student.to_dict() 
        students_dict.append(student_dict)

    if path is None:
        path = Path('src/lab08/students_output.json')
    with open(path, 'w', encoding = "utf-8") as f:
        json.dump(students_dict, f, ensure_ascii = False, indent = 2)
    print(f"Сохранено {len(students)} студентов в файл: {path}")


def students_from_json(path: str) -> List[Student]:
    if not Path(path).exists():
        raise FileNotFoundError
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)  # читаем JSON, получаем список
    except json.JSONDecodeError as e:
        raise ValueError
    students = []
    for item in data:
        student = Student.from_dict(item)
        students.append(student)
    return students
        

test_students = [
    Student("Иванов Иван", "2000-01-15", "SE-01", 4.5),
    Student("Петрова Анна", "2001-08-22", "SE-02", 4.8),
    Student("Сидоров Алексей", "1999-03-10", "CS-01", 3.9)
]
student_to_json(test_students, None)
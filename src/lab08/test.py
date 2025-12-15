# test_student.py
from models import Student

print("=== ТЕСТ 1: Создание студента ===")
# Создаём студента
student1 = Student(
    fio="Иванов Иван Иванович",
    birthdate="2000-05-15",
    group="SE-01",
    gpa=4.5
)

print(f"Создан студент: {student1}")
print(f"Тип объекта: {type(student1)}")

print("\n=== ТЕСТ 2: Проверка методов ===")
# Проверяем методы
print(f"Возраст студента: {student1.age()} лет")
print(f"Словарь студента: {student1.to_dict()}")

print("\n=== ТЕСТ 3: Создание из словаря ===")
# Создаём второго студента из словаря
data = {
    'fio': 'Петрова Анна Сергеевна',
    'birthdate': '2001-08-22',
    'group': 'SE-02',
    'gpa': 4.8
}

student2 = Student.from_dict(data)
print(f"Создан из словаря: {student2}")

print("\n=== ТЕСТ 4: Проверка валидации (ошибки) ===")
# Пробуем создать студента с ошибками
try:
    bad_student = Student(
        fio="Тестовый",
        birthdate="2000-13-45",  #  Неправильная дата
        group="TEST",
        gpa=3.0
    )
except ValueError as e:
    print(f"Ошибка даты (ожидаемо): {e}")

try:
    bad_student = Student(
        fio="Тестовый",
        birthdate="2000-01-01",
        group="TEST",
        gpa=10.0  #  GPA > 5
    )
except ValueError as e:
    print(f"Ошибка GPA (ожидаемо): {e}")

print("\n=== ТЕСТ 5: Работа с несколькими студентами ===")
students = [student1, student2]
for i, student in enumerate(students, 1):
    print(f"Студент {i}: {student}")
    print(f"   Возраст: {student.age()} лет")
    print(f"   Словарь: {student.to_dict()}")
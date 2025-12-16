## Лабораторная работа 8
### models.py
```python
from dataclasses import dataclass, field, asdict
from datetime import datetime, date
from typing import Optional
import re

@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float
    
    def __post_init__(self):
        """Валидация данных после инициализации"""
        # Валидация формата даты
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', self.birthdate):
            raise ValueError(f"Неверный формат даты: {self.birthdate}. Ожидается YYYY-MM-DD")
   
        # Проверка, что дата существует
        try:
            datetime.strptime(self.birthdate, '%Y-%m-%d')
        except ValueError:
            raise ValueError(f"Неверная дата: {self.birthdate}")
        
        # Валидация GPA
        if not 0 <= self.gpa <= 5:
            raise ValueError(f"GPA должен быть в диапазоне от 0 до 5, получено: {self.gpa}")
        
        # Валидация ФИО (должно содержать как минимум 2 слова)
        if len(self.fio.strip().split()) < 2:
            raise ValueError(f"ФИО должно содержать как минимум имя и фамилию: {self.fio}")
    
    def age(self) -> int:
        """Вычисление возраста студента в полных годах"""
        birth_date = datetime.strptime(self.birthdate, '%Y-%m-%d')
        today = date.today()
        
        age = today.year - birth_date.year
        # Корректировка, если день рождения еще не наступил в этом году
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        return age
    
    def to_dict(self) -> dict:
        """Сериализация объекта в словарь"""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Student':
        """Десериализация из словаря"""
        return cls(
            fio=data['fio'],
            birthdate=data['birthdate'],
            group=data['group'],
            gpa=float(data['gpa'])
        )
    
    def __str__(self) -> str:
        """Красивый вывод информации о студенте"""
        return f"{self.fio}\n" \
               f"Дата рождения: {self.birthdate} (Возраст: {self.age()} лет)\n" \
               f"Группа: {self.group}\n" \
               f"Средний балл: {self.gpa:.2f}"
    
    def __repr__(self) -> str:
        """Официальное строковое представление"""
        return f"Student(fio='{self.fio}', birthdate='{self.birthdate}', " \
               f"group='{self.group}', gpa={self.gpa})"
    

```

### serialize.py
```python
rom models import Student
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
```
### test.py
```python
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
```

## Лабораторная работа 9
### group.py
```python
import sys
import os
from dataclasses import dataclass
import csv
from pathlib import Path

# Полный путь к проекту
project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# Добавляем src в путь
sys.path.append(os.path.join(project_root, 'src'))
from lab08.models import Student
class Group:

    CSV_HEADER = ['fio', 'birthdate', 'group', 'gpa']

    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        
        # Создаем директорию если ее нет
        self.path.parent.mkdir(parents=True, exist_ok=True)
        
        # Если файла НЕТ ИЛИ он пустой - создаем/пересоздаем с заголовком
        if not self.path.exists() or os.path.getsize(self.path) == 0:
            with open(self.path, 'w', encoding='utf-8') as file:
                file.write("fio,birthdate,group,gpa\n")
            print(f"DEBUG: Создан/пересоздан файл {self.path}")
        else:
            print(f"DEBUG: Используем существующий файл {self.path}")

    def _read_all_(self):
        spisok = []
        try:
            with open(self.path, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                
                # Проверяем заголовок ТОЛЬКО ПОСЛЕ создания reader
                if reader.fieldnames is not None and reader.fieldnames != self.CSV_HEADER:
                    raise ValueError("Некорректный формат CSV-файла")
                
                for row in reader:
                    spisok.append(row)
                    
        except FileNotFoundError:
            # Если файл не найден, возвращаем пустой список
            return []
        except Exception as e:
            # Другие ошибки
            print(f"Ошибка при чтении файла: {e}")
            return []
        
        return spisok
    
    def _write_all(self, students):
        """Записывает всех студентов в CSV-файл."""
        with open(self.path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(self.CSV_HEADER)
            for student in students:
                writer.writerow([student.fio, student.birthdate, student.group, student.gpa])

    def list(self):
        students = []
        rows = self._read_all_()
        for row in rows:
            students.append( # Добавляем всех студентов в виде объектов Student
                Student(fio=row['fio'], birthdate=row['birthdate'], group=row['group'], gpa=float(row['gpa']))
            )
        return students  
    
    def add(self, student):
         with open(self.path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([student.fio, student.birthdate, student.group, student.gpa])

    def find(self, substr):
        all_students = self.list()
        substr_lower = substr.lower()
        found_students = []
        # Перебираем всех студентов
        for student in all_students:
            # Приводим ФИО студента к нижнему регистру
            student_fio_lower = student.fio.lower()
            
            # Проверяем, содержится ли подстрока в ФИО
            if substr_lower in student_fio_lower:
                # Если да - добавляем студента в список найденных
                found_students.append(student)
        
        # Возвращаем список найденных студентов
        return found_students
    
    def remove(self, fio):
        all_students = self.list()
        new_students = [student for student in all_students if student.fio != fio]
        
        if len(new_students) == len(all_students):
            return False  # Никто не удален
        
        self._write_all(new_students)
        return True

    def update(self, fio, **fields):
        all_students = self.list()
        updated = False
        
        for student in all_students:
            if student.fio == fio:
                # Обновляем указанные поля
                if 'fio' in fields:
                    student.fio = fields['fio']
                if 'birthdate' in fields:
                    student.birthdate = fields['birthdate']
                if 'group' in fields:
                    student.group = fields['group']
                if 'gpa' in fields:
                    student.gpa = float(fields['gpa'])
                updated = True
                break
        
        if updated:
            self._write_all(all_students)
        all_students = self.list()
        return updated
    
    def count(self) -> int:
        """Возвращает количество студентов."""
        return len(self.list())
    
    def stats(self):
        """
        Возвращает статистику по студентам в группе.
        
        Returns:
            Словарь со статистикой:
            {
                "count": общее количество студентов,
                "min_gpa": минимальный GPA,
                "max_gpa": максимальный GPA,
                "avg_gpa": средний GPA,
                "groups": распределение по группам,
                "top_5_students": топ-5 студентов по GPA
            }
        """
        # Получаем всех студентов
        students = self.list()
        # Если нет студентов - возвращаем пустую статистику
        if not students:
            return {
                "count": 0,
                "min_gpa": 0,
                "max_gpa": 0,
                "avg_gpa": 0,
                "groups": {},
                "top_5_students": []
            }
         # 1. Общее количество
        total_count = len(students)
        
        # 2. Статистика по GPA
        gpa_values = [student.gpa for student in students]
        min_gpa = min(gpa_values)
        max_gpa = max(gpa_values)
        avg_gpa = sum(gpa_values) / total_count

        # 3. Распределение по группам
        groups_distribution = {}
        for student in students:
            group_name = student.group
            if group_name in groups_distribution:
                groups_distribution[group_name] += 1
            else:
                groups_distribution[group_name] = 1

          # 4. Топ-5 студентов по GPA
        # Сортируем студентов по GPA в убывающем порядке
        sorted_students = sorted(students, key=lambda s: s.gpa, reverse=True)
        
        # Берем первых 5 (или меньше, если студентов меньше 5)
        top_5 = sorted_students[:5]
        
        # Преобразуем в список словарей
        top_5_list = [
            {"fio": student.fio, "gpa": student.gpa}
            for student in top_5
        ]
        
        # 5. Формируем итоговый словарь
        statistics = {
            "count": total_count,
            "min_gpa": min_gpa,
            "max_gpa": max_gpa,
            "avg_gpa": round(avg_gpa, 2),  # Округляем до 2 знаков
            "groups": groups_distribution,
            "top_5_students": top_5_list
        }
        
        return statistics
```

### test.py
```python
#!/usr/bin/env python3
"""
ФИНАЛЬНЫЙ РАБОЧИЙ ТЕСТ
"""

import tempfile
import os
import sys

sys.path.append('src')

from lab08.models import Student
from lab09.group import Group

print("🧪 ФИНАЛЬНЫЙ ТЕСТ")
print("=" * 40)

# Создаем пустой файл
temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, encoding='utf-8')
csv_path = temp_file.name
temp_file.close()

print(f"Файл: {csv_path}")

try:
    print("\n1. Создаем Group с пустым файлом...")
    group = Group(csv_path)  # Должен добавить заголовок
    
    print("\n2. Проверяем что в файле...")
    with open(csv_path, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"   Содержимое: {repr(content)}")
        assert content == "fio,birthdate,group,gpa\n", "Должен быть заголовок!"
    
    print("\n3. Добавляем студента (с полным ФИО!)...")
    student = Student("Иванов Иван Иванович", "2003-10-10", "БИВТ-21-1", 4.3)
    group.add(student)
    print("   ✅ Студент добавлен")
    
    print("\n4. Проверяем файл...")
    with open(csv_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        print(f"   Всего строк: {len(lines)}")
        for i, line in enumerate(lines):
            print(f"   Строка {i}: {repr(line)}")
    
    print("\n5. Проверяем list()...")
    students = group.list()
    print(f"   list() вернул: {len(students)} студентов")
    
    if students:
        print(f"   Первый студент: {students[0].fio}, GPA: {students[0].gpa}")
    
    print("\n6. Тестируем все методы CRUD...")
    
    print(f"   count(): {group.count()}")
    print(f"   find('Иванов'): {len(group.find('Иванов'))}")
    print(f"   update(): {group.update('Иванов Иван Иванович', gpa=4.5)}")
    print(f"   remove(): {group.remove('Иванов Иван Иванович')}")
    print(f"   После удаления: {group.count()}")
    
    print("\n🎉 ВСЁ РАБОТАЕТ КОРРЕКТНО!")
    
except AssertionError as e:
    print(f"\n❌ AssertionError: {e}")
except Exception as e:
    print(f"\n❌ ОШИБКА: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
finally:
    if os.path.exists(csv_path):
        os.unlink(csv_path)
        print(f"\n🗑️  Файл удален")
```
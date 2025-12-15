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

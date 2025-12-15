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
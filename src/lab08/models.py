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
    

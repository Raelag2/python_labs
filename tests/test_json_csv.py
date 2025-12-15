import pytest

# from src.lib.text import normalize, tokenize, count_freq, top_n # Не работает, пишет - нет модуля src
import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)  # Добавили путь в папку с функциями
from src.lab05.json_csv import json_to_csv, csv_to_json


# Проверка функции json_to_csv
@pytest.mark.parametrize(  # Создаём параметрайз с 3 запусками тестов
    "path_in, path_out, expected",  # Получаем ссылку исходный файл, на файл записи и ожидаемый вывод
    [
        (
            "././data/samples/people.json",
            "././data/out/people07.csv",
            None,
        ),  # Если ошибок нет, функция ничего не выдаст
        (
            "././data/samples/pustoy07.json",
            "././data/out/pustoy07.csv",
            ValueError,
        ),  # Если исходный файл пустой, ожидаем ошибку ValueError
        (
            "././data/samples/net_fayla07.json",
            "././data/out/net_fayla07.csv",
            FileNotFoundError,
        ),  # Если исходный файл не существует, ожидаем FileNotFoundError
    ],
)
def test_json_to_csv_basic(path_in, path_out, expected):
    if expected is None:  # Если ожидаемое поведение — тест успешно пройден
        assert json_to_csv(path_in, path_out) == expected
    else:  # Если ожидаем ошибку:
        with pytest.raises(expected):  # Совместно с модулем исключения ошибок
            json_to_csv(
                path_in, path_out
            )  # Запускаем функцию. Если ошибка соответствует значению expected, тест пройден


# Проверка функции csv_to_json
@pytest.mark.parametrize(
    "path_in, path_out, expected",  # Получаем ссылку исходный файл, на файл записи и ожидаемый вывод
    [
        (
            "././data/samples/people1.csv",
            "././data/out/people07.json",
            None,
        ),  # Если ошибок нет, функция ничего не выдаст
        (
            "././data/samples/pustoy07.csv",
            "././data/out/pustoy07.json",
            ValueError,
        ),  # Если исходный файл пустой, ожидаем ошибку ValueError
        (
            "././data/samples/net_fayla07.csv",
            "././data/out/net_fayla07.json",
            FileNotFoundError,
        ),  # Если исходный файл не существует, ожидаем FileNotFoundError
    ],
)
def test_csv_to_json_basic(path_in, path_out, expected):
    if expected is None:  # Если получено ожидаемое поведение — тест успешно пройден
        assert csv_to_json(path_in, path_out) == expected
    else:  # Если ожидаем ошибку:
        with pytest.raises(expected):  # Совместно с модулем исключения ошибок
            csv_to_json(
                path_in, path_out
            )  # Запускаем функцию. Если ошибка соответствует значению expected, тест пройден


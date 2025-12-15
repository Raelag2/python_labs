import pytest
import sys
from pathlib import Path

# Добавляем директорию с модулями в путь поиска
current_dir = Path(__file__).parent
project_root = current_dir.parent
sys.path.insert(0, str(project_root))

# Импортируем функции для тестирования
from src.lib.text import normalize, tokenize, count_freq, top_n


def test_normalization_with_different_inputs():
    """Тестируем функцию normalize с различными входными данными."""
    
    test_cases = [
        ("ПрИвЕт \nМИр \t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello \r \nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
    ]
    
    for input_text, expected_output in test_cases:
        result = normalize(input_text, casefold=True, yo2e=True)
        assert result == expected_output, f"Ошибка для '{input_text}': получено '{result}', ожидалось '{expected_output}'"


def test_tokenization_of_various_texts():
    """Проверяем разбиение текста на токены."""
    
    test_scenarios = [
        ("hello,world!!!", ["hello", "world"]),
        ("это по-настоящему круто", ["это", "по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
    ]
    
    for source_text, expected_tokens in test_scenarios:
        token_list = tokenize(source_text)
        assert token_list == expected_tokens, f"Ошибка токенизации для '{source_text}': {token_list} != {expected_tokens}"


def test_frequency_counting_and_ranking():
    """Тестируем подсчет частот и получение топ-N."""
    
    # Подсчет частот
    frequency_data = [
        (["a", "b", "a", "c", "b", "a"], {"a": 3, "b": 2, "c": 1}),
        (["bb", "aa", "bb", "aa", "cc"], {"aa": 2, "bb": 2, "cc": 1}),
    ]
    
    for word_list, expected_freq_dict in frequency_data:
        frequency_result = count_freq(word_list)
        assert frequency_result == expected_freq_dict, f"Ошибка подсчета частот: {frequency_result} != {expected_freq_dict}"
    
    # Проверка топ-N результатов
    ranking_test_cases = [
        ({"a": 3, "b": 2, "c": 1}, 2, [("a", 3), ("b", 2)]),
        ({"aa": 2, "bb": 2, "cc": 1}, 5, [("aa", 2), ("bb", 2), ("cc", 1)]),
    ]
    
    for freq_dict, n, expected_top in ranking_test_cases:
        top_results = top_n(freq_dict, n)
        assert top_results == expected_top, f"Ошибка топ-{n}: {top_results} != {expected_top}"


def test_edge_cases():
    """Проверяем крайние случаи."""
    
    # Пустая строка
    assert normalize("", casefold=True, yo2e=True) == ""
    
    # Пустой список токенов
    assert count_freq([]) == {}
    
    # Топ-0 из пустого словаря
    assert top_n({}, 0) == []
    
    # Топ больше, чем элементов
    assert top_n({"a": 1}, 10) == [("a", 1)]


if __name__ == "__main__":
    # Для ручного запуска тестов
    test_normalization_with_different_inputs()
    test_tokenization_of_various_texts()
    test_frequency_counting_and_ranking()
    test_edge_cases()
    print("Все тесты пройдены успешно!")

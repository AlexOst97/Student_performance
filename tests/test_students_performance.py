from src.read_files import students_performance
from tests.conftest import table_1, dict_1


def test_students_performance_1(table_1):
    """Тестирование корректного расчета рейтинга студентов"""
    assert students_performance(dict_1) == table_1


def test_students_performance_2():
    """Тестирование валидации типа входных данных"""
    assert students_performance("abc") == "Ошибка: ожидается тип данных 'словарь'"


def test_students_performance_3():
    """Тестирование обработки пустого словаря входных данных"""
    assert students_performance({}) == []


def test_students_performance_4():
    """Тестирование обработки ошибки сохранения отчета в несуществующую директорию"""
    data = {"Иванов": [5]}
    result = students_performance(data, "/abc/result.txt")
    assert (
        result
        == "Ошибка при сохранении отчета: [Errno 2] No such file or directory: '/abc/result.txt'"
    )

from src.read_files import students_report
from tests.conftest import report_1, list_1


def test_students_report_1(report_1):
    """Тестирование корректного формирования отчета из валидных данных"""
    assert students_report(list_1) == report_1


def test_students_report_2():
    """Тестирование валидации типа входных данных"""
    assert students_report("abc") == "Ошибка: ожидается тип данных 'список'"


def test_students_report_3():
    """Тестирование обработки ошибки доступа"""
    assert (
        students_report(["abc"])
        == "Возникла ошибка: string indices must be integers, not 'str'"
    )


def test_students_report_4():
    """Тестирование обработки нечисловых значений в поле оценки"""
    data = [{"student_name": "Иванов", "subject": "Математика", "grade": "abc"}]
    assert (
        students_report(data)
        == "Возникла ошибка: invalid literal for int() with base 10: 'abc'"
    )


def test_students_report_5():
    """Тестирование обработки отсутствия обязательного поля 'grade'"""
    data = [{"student_name": "Иванов"}]
    assert students_report(data) == "Возникла ошибка: 'grade'"

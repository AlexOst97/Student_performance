from src.read_files import read_csv_files
from unittest.mock import Mock


def test_read_csv_files_1():
    """Тестирование функции с корректными параметрами"""
    mock_read_csv_files = Mock(return_value=r"..\\files\\students1.csv")
    read_csv_files = mock_read_csv_files
    read_csv_files(file_json=r"..\\files\\students1.csv") == r"..\\files\\students1.csv"
    mock_read_csv_files.assert_called_once_with(file_json=r"..\\files\\students1.csv")


def test_read_csv_files_2():
    """Тестирование функции при чтении несуществующего файла"""
    assert read_csv_files("") == "Ошибка: [Errno 2] No such file or directory: ''"

import csv
from collections import defaultdict
from tabulate import tabulate


def read_csv_files(filenames):
    """Чтение данных из CSV файлов"""
    list_csv = []

    if isinstance(filenames, str):
        filenames = [filenames]

    for filename in filenames:
        try:
            with open(f"{filename}", encoding="utf-8") as file_csv:
                reader = csv.DictReader(file_csv)
                for row in reader:
                    list_csv.append(row)

        except Exception as error:
            return f"Ошибка: {error}"

    return list_csv


def students_report(list_csv):
    """Отчет о студентов"""
    report = defaultdict(list)

    try:
        if not isinstance(list_csv, list):
            return "Ошибка: ожидается тип данных 'список'"

        for students in list_csv:
            student_name = students["student_name"]
            grade = int(students["grade"])
            report[student_name].append(grade)
        return dict(report)
    except Exception as e:
        return f"Возникла ошибка: {e}"


def students_performance(report, report_file=None):
    """Создание таблицы о успеваемости студентов"""

    # Создаем список студентов со средними оценками
    students_list = []
    try:
        if not isinstance(report, dict):
            return "Ошибка: ожидается тип данных 'словарь'"
        for student, grades in report.items():
            average_grade = sum(grades) / len(grades)
            students_list.append((student, round(average_grade, 2)))
    except Exception as e:
        return f"Возникла ошибка: {e}"

    students_list.sort(key=lambda x: x[1], reverse=True)

    # Создаем таблицу
    table_data = []
    for i, (student, avg_grade) in enumerate(students_list, 1):
        table_data.append([i, student, avg_grade])

    headers = ["№", "student_name", "grade"]
    table = tabulate(table_data, headers=headers, tablefmt="grid")

    # Сохранение в файл
    if report_file:
        try:
            with open(report_file, "w", encoding="utf-8") as f:
                f.write(table)
            return f"Отчет сохранен в файл: {report_file}"
        except Exception as e:
            return f"Ошибка при сохранении отчета: {e}"

    return students_list

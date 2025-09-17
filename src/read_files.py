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
        for students in list_csv:
            student_name = students['student_name']
            grade = int(students['grade'])
            report[student_name].append(grade)
        return dict(report)
    except Exception as e:
        print(f"Возникла ошибка: {e}")


def students_performance(report, output_file=None):
    """Создание таблицы о успеваемости студентов"""

    # Создаем список студентов со средними оценками
    students_list = []
    for student, grades in report.items():
        average_grade = sum(grades) / len(grades)
        students_list.append((student, round(average_grade, 2)))

    students_list.sort(key=lambda x: x[1], reverse=True)

    # Создаем таблицу
    table_data = []
    for i, (student, avg_grade) in enumerate(students_list, 1):
        table_data.append([i, student, avg_grade])

    headers = ["№", "student_name", "grade"]
    table = tabulate(table_data, headers=headers, tablefmt="grid")
    print(table)

    # Сохранение в файл
    if output_file:
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(table)
            print(f"Отчет сохранен в файл: {output_file}")
        except Exception as e:
            print(f"Ошибка при сохранении отчета: {e}")

    return students_list

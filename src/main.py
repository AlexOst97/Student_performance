from read_files import read_csv_files, students_report, students_performance
import argparse


def main():
    parser = argparse.ArgumentParser(description='Анализ успеваемости студентов')
    parser.add_argument('--files', nargs='+', required=True, help='Список CSV файлов для анализа')
    parser.add_argument('--report', help='Имя файла для сохранения отчета')

    args = parser.parse_args()

    # Чтение данных из файлов
    data = read_csv_files(args.files)


    # Создание отчета
    report = students_report(data)

    # Вывод производительности
    students_performance(report, args.report)

if __name__ == "__main__":
    main()
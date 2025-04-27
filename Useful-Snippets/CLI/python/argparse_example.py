#!/usr/bin/env python3
"""
Пример использования argparse для парсинга аргументов командной строки.

Этот скрипт демонстрирует различные возможности argparse:
- Позиционные аргументы
- Опциональные аргументы
- Аргументы с выбором из списка
- Аргументы с типом данных
- Аргументы с действиями (store_true, store_false)
- Группы аргументов
- Подкоманды
"""

import argparse
import sys


def create_parser():
    """
    Создает парсер аргументов командной строки.
    
    Returns:
        argparse.ArgumentParser: Парсер аргументов
    """
    # Создаем основной парсер
    parser = argparse.ArgumentParser(
        description='Пример использования argparse',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    # Добавляем позиционные аргументы
    parser.add_argument(
        'input_file',
        help='Входной файл'
    )

    # Добавляем опциональные аргументы
    parser.add_argument(
        '-o', '--output',
        help='Выходной файл',
        default='output.txt'
    )

    # Добавляем аргумент с выбором из списка
    parser.add_argument(
        '--format',
        choices=['txt', 'json', 'xml'],
        default='txt',
        help='Формат выходного файла'
    )

    # Добавляем аргумент с типом данных
    parser.add_argument(
        '--number',
        type=int,
        help='Число'
    )

    # Добавляем аргумент с действием
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Включить подробный вывод'
    )

    # Создаем группу аргументов
    group = parser.add_argument_group('Дополнительные опции')
    group.add_argument(
        '--encoding',
        default='utf-8',
        help='Кодировка файлов'
    )
    group.add_argument(
        '--buffer-size',
        type=int,
        default=8192,
        help='Размер буфера'
    )

    # Создаем подкоманды
    subparsers = parser.add_subparsers(dest='command', help='Доступные команды')

    # Парсер для команды process
    process_parser = subparsers.add_parser('process', help='Обработать файл')
    process_parser.add_argument(
        '--method',
        choices=['method1', 'method2'],
        default='method1',
        help='Метод обработки'
    )

    # Парсер для команды convert
    convert_parser = subparsers.add_parser('convert', help='Конвертировать файл')
    convert_parser.add_argument(
        '--target-format',
        choices=['txt', 'json', 'xml'],
        required=True,
        help='Целевой формат'
    )

    return parser


def main():
    """
    Основная функция.
    """
    parser = create_parser()
    args = parser.parse_args()

    # Выводим все аргументы
    if args.verbose:
        print('Аргументы командной строки:')
        for arg in vars(args):
            print(f'{arg}: {getattr(args, arg)}')

    # Обрабатываем команды
    if args.command == 'process':
        print(f'Обработка файла {args.input_file} методом {args.method}')
    elif args.command == 'convert':
        print(f'Конвертация файла {args.input_file} в формат {args.target_format}')
    else:
        print(f'Обработка файла {args.input_file} в формат {args.format}')


if __name__ == '__main__':
    main() 
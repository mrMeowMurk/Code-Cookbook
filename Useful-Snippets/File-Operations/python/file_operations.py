#!/usr/bin/env python3
"""
Примеры работы с файлами в Python.

Этот скрипт демонстрирует различные операции с файлами:
- Чтение текстовых файлов
- Запись текстовых файлов
- Чтение бинарных файлов
- Запись бинарных файлов
- Работа с большими файлами
- Буферизованное чтение/запись
"""

import os
import json
import csv
import logging
from typing import List, Dict, Any, Generator
from pathlib import Path


def read_text_file(file_path: str) -> str:
    """
    Чтение текстового файла.
    
    Args:
        file_path (str): Путь к файлу
        
    Returns:
        str: Содержимое файла
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def write_text_file(file_path: str, content: str) -> None:
    """
    Запись в текстовый файл.
    
    Args:
        file_path (str): Путь к файлу
        content (str): Содержимое для записи
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def read_binary_file(file_path: str) -> bytes:
    """
    Чтение бинарного файла.
    
    Args:
        file_path (str): Путь к файлу
        
    Returns:
        bytes: Содержимое файла
    """
    with open(file_path, 'rb') as file:
        return file.read()


def write_binary_file(file_path: str, content: bytes) -> None:
    """
    Запись в бинарный файл.
    
    Args:
        file_path (str): Путь к файлу
        content (bytes): Содержимое для записи
    """
    with open(file_path, 'wb') as file:
        file.write(content)


def read_large_file(file_path: str, chunk_size: int = 8192) -> Generator[str, None, None]:
    """
    Чтение большого файла по частям.
    
    Args:
        file_path (str): Путь к файлу
        chunk_size (int): Размер части
        
    Yields:
        str: Часть файла
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk


def read_json_file(file_path: str) -> Dict[str, Any]:
    """
    Чтение JSON файла.
    
    Args:
        file_path (str): Путь к файлу
        
    Returns:
        Dict[str, Any]: Данные из файла
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def write_json_file(file_path: str, data: Dict[str, Any], indent: int = 4) -> None:
    """
    Запись в JSON файл.
    
    Args:
        file_path (str): Путь к файлу
        data (Dict[str, Any]): Данные для записи
        indent (int): Отступ для форматирования
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=indent, ensure_ascii=False)


def read_csv_file(file_path: str) -> List[Dict[str, str]]:
    """
    Чтение CSV файла.
    
    Args:
        file_path (str): Путь к файлу
        
    Returns:
        List[Dict[str, str]]: Данные из файла
    """
    with open(file_path, 'r', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)


def write_csv_file(file_path: str, data: List[Dict[str, str]], fieldnames: List[str]) -> None:
    """
    Запись в CSV файл.
    
    Args:
        file_path (str): Путь к файлу
        data (List[Dict[str, str]]): Данные для записи
        fieldnames (List[str]): Имена полей
    """
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def setup_logging(log_file: str, level: int = logging.INFO) -> None:
    """
    Настройка логирования.
    
    Args:
        log_file (str): Путь к файлу лога
        level (int): Уровень логирования
    """
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )


def main():
    """
    Основная функция.
    """
    # Создаем тестовые данные
    test_data = {
        'name': 'John Doe',
        'age': 30,
        'email': 'john@example.com'
    }
    
    # Записываем JSON файл
    write_json_file('test.json', test_data)
    
    # Читаем JSON файл
    data = read_json_file('test.json')
    print('JSON данные:', data)
    
    # Создаем CSV данные
    csv_data = [
        {'name': 'John', 'age': '30', 'email': 'john@example.com'},
        {'name': 'Jane', 'age': '25', 'email': 'jane@example.com'}
    ]
    
    # Записываем CSV файл
    write_csv_file('test.csv', csv_data, ['name', 'age', 'email'])
    
    # Читаем CSV файл
    data = read_csv_file('test.csv')
    print('CSV данные:', data)
    
    # Настраиваем логирование
    setup_logging('test.log')
    logging.info('Тестовое сообщение')
    
    # Очищаем тестовые файлы
    os.remove('test.json')
    os.remove('test.csv')
    os.remove('test.log')


if __name__ == '__main__':
    main() 
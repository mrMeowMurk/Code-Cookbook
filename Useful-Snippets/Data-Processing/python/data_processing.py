#!/usr/bin/env python3
"""
Примеры обработки данных в Python.

Этот скрипт демонстрирует различные операции с данными:
- Работа с датами и временем
- Форматирование строк
- Конвертация типов
- Сериализация/десериализация
- Работа с коллекциями
- Фильтрация и сортировка
"""

import json
import datetime
import pytz
from typing import List, Dict, Any, Union
from collections import defaultdict, Counter
from dataclasses import dataclass, asdict


# Работа с датами и временем
def parse_date(date_str: str, format_str: str = '%Y-%m-%d') -> datetime.datetime:
    """
    Парсинг даты из строки.
    
    Args:
        date_str (str): Строка с датой
        format_str (str): Формат даты
        
    Returns:
        datetime.datetime: Объект даты
    """
    return datetime.datetime.strptime(date_str, format_str)


def format_date(date: datetime.datetime, format_str: str = '%Y-%m-%d') -> str:
    """
    Форматирование даты в строку.
    
    Args:
        date (datetime.datetime): Объект даты
        format_str (str): Формат даты
        
    Returns:
        str: Отформатированная дата
    """
    return date.strftime(format_str)


def add_timezone(date: datetime.datetime, timezone: str) -> datetime.datetime:
    """
    Добавление временной зоны к дате.
    
    Args:
        date (datetime.datetime): Объект даты
        timezone (str): Временная зона
        
    Returns:
        datetime.datetime: Дата с временной зоной
    """
    tz = pytz.timezone(timezone)
    return tz.localize(date)


def date_range(start_date: datetime.datetime, end_date: datetime.datetime, step: datetime.timedelta) -> List[datetime.datetime]:
    """
    Генерация диапазона дат.
    
    Args:
        start_date (datetime.datetime): Начальная дата
        end_date (datetime.datetime): Конечная дата
        step (datetime.timedelta): Шаг
        
    Returns:
        List[datetime.datetime]: Список дат
    """
    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date)
        current_date += step
    return dates


# Форматирование строк
def format_string(template: str, **kwargs) -> str:
    """
    Форматирование строки с использованием шаблона.
    
    Args:
        template (str): Шаблон строки
        **kwargs: Параметры для подстановки
        
    Returns:
        str: Отформатированная строка
    """
    return template.format(**kwargs)


def format_f_string(name: str, age: int) -> str:
    """
    Форматирование строки с использованием f-строки.
    
    Args:
        name (str): Имя
        age (int): Возраст
        
    Returns:
        str: Отформатированная строка
    """
    return f'Имя: {name}, Возраст: {age}'


# Конвертация типов
def convert_types(value: Any, target_type: type) -> Any:
    """
    Конвертация значения в указанный тип.
    
    Args:
        value (Any): Исходное значение
        target_type (type): Целевой тип
        
    Returns:
        Any: Конвертированное значение
    """
    return target_type(value)


# Сериализация/десериализация
@dataclass
class Person:
    """
    Класс для представления человека.
    """
    name: str
    age: int
    email: str


def serialize_person(person: Person) -> str:
    """
    Сериализация объекта Person в JSON.
    
    Args:
        person (Person): Объект Person
        
    Returns:
        str: JSON строка
    """
    return json.dumps(asdict(person))


def deserialize_person(json_str: str) -> Person:
    """
    Десериализация JSON в объект Person.
    
    Args:
        json_str (str): JSON строка
        
    Returns:
        Person: Объект Person
    """
    data = json.loads(json_str)
    return Person(**data)


# Работа с коллекциями
def group_by(items: List[Dict[str, Any]], key: str) -> Dict[str, List[Dict[str, Any]]]:
    """
    Группировка элементов по ключу.
    
    Args:
        items (List[Dict[str, Any]]): Список элементов
        key (str): Ключ для группировки
        
    Returns:
        Dict[str, List[Dict[str, Any]]]: Сгруппированные элементы
    """
    groups = defaultdict(list)
    for item in items:
        groups[item[key]].append(item)
    return dict(groups)


def count_items(items: List[Any]) -> Dict[Any, int]:
    """
    Подсчет количества элементов.
    
    Args:
        items (List[Any]): Список элементов
        
    Returns:
        Dict[Any, int]: Словарь с количеством элементов
    """
    return dict(Counter(items))


# Фильтрация и сортировка
def filter_items(items: List[Any], condition: callable) -> List[Any]:
    """
    Фильтрация элементов по условию.
    
    Args:
        items (List[Any]): Список элементов
        condition (callable): Функция-условие
        
    Returns:
        List[Any]: Отфильтрованные элементы
    """
    return list(filter(condition, items))


def sort_items(items: List[Any], key: callable = None, reverse: bool = False) -> List[Any]:
    """
    Сортировка элементов.
    
    Args:
        items (List[Any]): Список элементов
        key (callable): Функция для извлечения ключа сортировки
        reverse (bool): Флаг обратной сортировки
        
    Returns:
        List[Any]: Отсортированные элементы
    """
    return sorted(items, key=key, reverse=reverse)


def main():
    """
    Основная функция.
    """
    # Работа с датами
    date = parse_date('2023-01-01')
    print('Парсинг даты:', date)
    
    formatted_date = format_date(date)
    print('Форматирование даты:', formatted_date)
    
    date_with_tz = add_timezone(date, 'Europe/Moscow')
    print('Дата с временной зоной:', date_with_tz)
    
    dates = date_range(date, date + datetime.timedelta(days=5), datetime.timedelta(days=1))
    print('Диапазон дат:', [format_date(d) for d in dates])
    
    # Форматирование строк
    template = 'Привет, {name}! Тебе {age} лет.'
    formatted = format_string(template, name='John', age=30)
    print('Форматирование строки:', formatted)
    
    f_string = format_f_string('John', 30)
    print('F-строка:', f_string)
    
    # Конвертация типов
    number = convert_types('123', int)
    print('Конвертация в число:', number)
    
    # Сериализация/десериализация
    person = Person('John', 30, 'john@example.com')
    json_str = serialize_person(person)
    print('Сериализация:', json_str)
    
    deserialized_person = deserialize_person(json_str)
    print('Десериализация:', deserialized_person)
    
    # Работа с коллекциями
    items = [
        {'name': 'John', 'age': 30},
        {'name': 'Jane', 'age': 25},
        {'name': 'John', 'age': 35}
    ]
    
    grouped = group_by(items, 'name')
    print('Группировка:', grouped)
    
    counted = count_items([1, 2, 2, 3, 3, 3])
    print('Подсчет элементов:', counted)
    
    # Фильтрация и сортировка
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    filtered = filter_items(numbers, lambda x: x % 2 == 0)
    print('Фильтрация четных чисел:', filtered)
    
    sorted_numbers = sort_items(numbers, reverse=True)
    print('Сортировка по убыванию:', sorted_numbers)


if __name__ == '__main__':
    main() 
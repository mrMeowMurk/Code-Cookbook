#!/usr/bin/env python3
"""
Пример использования регулярных выражений для валидации данных.

Этот скрипт демонстрирует различные регулярные выражения для валидации:
- Email адреса
- Телефонные номера
- URL
- IP адреса
- Даты
- Пароли
"""

import re
from typing import Tuple


def validate_email(email: str) -> Tuple[bool, str]:
    """
    Валидация email адреса.
    
    Args:
        email (str): Email адрес
        
    Returns:
        Tuple[bool, str]: (Результат валидации, Сообщение об ошибке)
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True, ''
    return False, 'Неверный формат email адреса'


def validate_phone(phone: str) -> Tuple[bool, str]:
    """
    Валидация телефонного номера.
    
    Args:
        phone (str): Телефонный номер
        
    Returns:
        Tuple[bool, str]: (Результат валидации, Сообщение об ошибке)
    """
    # Удаляем все нецифровые символы
    digits = re.sub(r'\D', '', phone)
    
    # Проверяем длину и формат
    if len(digits) == 11 and digits.startswith(('7', '8')):
        return True, ''
    return False, 'Неверный формат телефонного номера'


def validate_url(url: str) -> Tuple[bool, str]:
    """
    Валидация URL.
    
    Args:
        url (str): URL
        
    Returns:
        Tuple[bool, str]: (Результат валидации, Сообщение об ошибке)
    """
    pattern = r'^https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    if re.match(pattern, url):
        return True, ''
    return False, 'Неверный формат URL'


def validate_ip(ip: str) -> Tuple[bool, str]:
    """
    Валидация IP адреса.
    
    Args:
        ip (str): IP адрес
        
    Returns:
        Tuple[bool, str]: (Результат валидации, Сообщение об ошибке)
    """
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if not re.match(pattern, ip):
        return False, 'Неверный формат IP адреса'
    
    # Проверяем, что каждое число в диапазоне 0-255
    numbers = ip.split('.')
    for num in numbers:
        if not 0 <= int(num) <= 255:
            return False, 'IP адрес содержит числа вне допустимого диапазона'
    
    return True, ''


def validate_date(date: str) -> Tuple[bool, str]:
    """
    Валидация даты в формате DD.MM.YYYY.
    
    Args:
        date (str): Дата
        
    Returns:
        Tuple[bool, str]: (Результат валидации, Сообщение об ошибке)
    """
    pattern = r'^(0[1-9]|[12]\d|3[01])\.(0[1-9]|1[0-2])\.\d{4}$'
    if not re.match(pattern, date):
        return False, 'Неверный формат даты'
    
    # Проверяем корректность даты
    day, month, year = map(int, date.split('.'))
    if month in [4, 6, 9, 11] and day > 30:
        return False, 'Неверное количество дней в месяце'
    elif month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            if day > 29:
                return False, 'Неверное количество дней в феврале високосного года'
        elif day > 28:
            return False, 'Неверное количество дней в феврале'
    
    return True, ''


def validate_password(password: str) -> Tuple[bool, str]:
    """
    Валидация пароля.
    
    Требования к паролю:
    - Минимум 8 символов
    - Минимум одна заглавная буква
    - Минимум одна строчная буква
    - Минимум одна цифра
    - Минимум один специальный символ
    
    Args:
        password (str): Пароль
        
    Returns:
        Tuple[bool, str]: (Результат валидации, Сообщение об ошибке)
    """
    if len(password) < 8:
        return False, 'Пароль должен содержать минимум 8 символов'
    
    if not re.search(r'[A-Z]', password):
        return False, 'Пароль должен содержать минимум одну заглавную букву'
    
    if not re.search(r'[a-z]', password):
        return False, 'Пароль должен содержать минимум одну строчную букву'
    
    if not re.search(r'\d', password):
        return False, 'Пароль должен содержать минимум одну цифру'
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, 'Пароль должен содержать минимум один специальный символ'
    
    return True, ''


def main():
    """
    Основная функция.
    """
    # Тестируем валидацию email
    email = 'user@example.com'
    is_valid, message = validate_email(email)
    print(f'Email {email}: {"валидный" if is_valid else "невалидный"}')
    if not is_valid:
        print(f'Ошибка: {message}')
    
    # Тестируем валидацию телефона
    phone = '+7 (999) 123-45-67'
    is_valid, message = validate_phone(phone)
    print(f'Телефон {phone}: {"валидный" if is_valid else "невалидный"}')
    if not is_valid:
        print(f'Ошибка: {message}')
    
    # Тестируем валидацию URL
    url = 'https://example.com'
    is_valid, message = validate_url(url)
    print(f'URL {url}: {"валидный" if is_valid else "невалидный"}')
    if not is_valid:
        print(f'Ошибка: {message}')
    
    # Тестируем валидацию IP
    ip = '192.168.1.1'
    is_valid, message = validate_ip(ip)
    print(f'IP {ip}: {"валидный" if is_valid else "невалидный"}')
    if not is_valid:
        print(f'Ошибка: {message}')
    
    # Тестируем валидацию даты
    date = '31.12.2023'
    is_valid, message = validate_date(date)
    print(f'Дата {date}: {"валидная" if is_valid else "невалидная"}')
    if not is_valid:
        print(f'Ошибка: {message}')
    
    # Тестируем валидацию пароля
    password = 'Password123!'
    is_valid, message = validate_password(password)
    print(f'Пароль {password}: {"валидный" if is_valid else "невалидный"}')
    if not is_valid:
        print(f'Ошибка: {message}')


if __name__ == '__main__':
    main() 
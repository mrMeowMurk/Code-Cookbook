#!/usr/bin/env python3
"""
Примеры работы с безопасностью в Python.

Этот скрипт демонстрирует различные операции с безопасностью:
- Хеширование паролей
- Шифрование данных
- Генерация токенов
- Работа с SSL/TLS
- Безопасное хранение данных
- Аутентификация и авторизация
"""

import os
import json
import base64
import hashlib
import secrets
import bcrypt
import jwt
from datetime import datetime, timedelta
from typing import Dict, Any, Tuple
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization


# Хеширование паролей
def hash_password(password: str) -> Tuple[str, str]:
    """
    Хеширование пароля с использованием bcrypt.
    
    Args:
        password (str): Пароль
        
    Returns:
        Tuple[str, str]: (Хеш пароля, Соль)
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode(), salt.decode()


def verify_password(password: str, hashed: str) -> bool:
    """
    Верификация пароля.
    
    Args:
        password (str): Пароль
        hashed (str): Хеш пароля
        
    Returns:
        bool: Результат верификации
    """
    return bcrypt.checkpw(password.encode(), hashed.encode())


# Шифрование данных
def generate_key() -> bytes:
    """
    Генерация ключа для шифрования.
    
    Returns:
        bytes: Ключ
    """
    return Fernet.generate_key()


def encrypt_data(data: str, key: bytes) -> str:
    """
    Шифрование данных.
    
    Args:
        data (str): Данные для шифрования
        key (bytes): Ключ
        
    Returns:
        str: Зашифрованные данные
    """
    f = Fernet(key)
    return f.encrypt(data.encode()).decode()


def decrypt_data(encrypted_data: str, key: bytes) -> str:
    """
    Расшифровка данных.
    
    Args:
        encrypted_data (str): Зашифрованные данные
        key (bytes): Ключ
        
    Returns:
        str: Расшифрованные данные
    """
    f = Fernet(key)
    return f.decrypt(encrypted_data.encode()).decode()


# Генерация токенов
def generate_jwt(payload: Dict[str, Any], secret: str, expires_in: int = 3600) -> str:
    """
    Генерация JWT токена.
    
    Args:
        payload (Dict[str, Any]): Данные токена
        secret (str): Секретный ключ
        expires_in (int): Время жизни токена в секундах
        
    Returns:
        str: JWT токен
    """
    payload['exp'] = datetime.utcnow() + timedelta(seconds=expires_in)
    return jwt.encode(payload, secret, algorithm='HS256')


def verify_jwt(token: str, secret: str) -> Dict[str, Any]:
    """
    Верификация JWT токена.
    
    Args:
        token (str): JWT токен
        secret (str): Секретный ключ
        
    Returns:
        Dict[str, Any]: Данные токена
    """
    return jwt.decode(token, secret, algorithms=['HS256'])


# Работа с SSL/TLS
def generate_rsa_key_pair() -> Tuple[bytes, bytes]:
    """
    Генерация пары RSA ключей.
    
    Returns:
        Tuple[bytes, bytes]: (Приватный ключ, Публичный ключ)
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    
    public_pem = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    
    return private_pem, public_pem


def sign_data(data: str, private_key: bytes) -> bytes:
    """
    Подпись данных.
    
    Args:
        data (str): Данные для подписи
        private_key (bytes): Приватный ключ
        
    Returns:
        bytes: Подпись
    """
    private_key = serialization.load_pem_private_key(
        private_key,
        password=None
    )
    
    signature = private_key.sign(
        data.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    
    return signature


def verify_signature(data: str, signature: bytes, public_key: bytes) -> bool:
    """
    Верификация подписи.
    
    Args:
        data (str): Данные
        signature (bytes): Подпись
        public_key (bytes): Публичный ключ
        
    Returns:
        bool: Результат верификации
    """
    public_key = serialization.load_pem_public_key(public_key)
    
    try:
        public_key.verify(
            signature,
            data.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False


# Безопасное хранение данных
def mask_sensitive_data(data: str, mask_char: str = '*') -> str:
    """
    Маскирование чувствительных данных.
    
    Args:
        data (str): Данные
        mask_char (str): Символ маски
        
    Returns:
        str: Замаскированные данные
    """
    if len(data) <= 4:
        return mask_char * len(data)
    return data[:2] + mask_char * (len(data) - 4) + data[-2:]


def anonymize_data(data: Dict[str, Any], fields: List[str]) -> Dict[str, Any]:
    """
    Анонимизация данных.
    
    Args:
        data (Dict[str, Any]): Данные
        fields (List[str]): Поля для анонимизации
        
    Returns:
        Dict[str, Any]: Анонимизированные данные
    """
    anonymized = data.copy()
    for field in fields:
        if field in anonymized:
            anonymized[field] = mask_sensitive_data(str(anonymized[field]))
    return anonymized


# Аутентификация и авторизация
class User:
    """
    Класс для представления пользователя.
    """
    def __init__(self, username: str, password: str, roles: List[str]):
        self.username = username
        self.password_hash, self.salt = hash_password(password)
        self.roles = roles


class AuthService:
    """
    Сервис аутентификации и авторизации.
    """
    def __init__(self, secret: str):
        self.secret = secret
        self.users: Dict[str, User] = {}
    
    def register_user(self, username: str, password: str, roles: List[str]) -> None:
        """
        Регистрация пользователя.
        
        Args:
            username (str): Имя пользователя
            password (str): Пароль
            roles (List[str]): Роли
        """
        self.users[username] = User(username, password, roles)
    
    def authenticate(self, username: str, password: str) -> str:
        """
        Аутентификация пользователя.
        
        Args:
            username (str): Имя пользователя
            password (str): Пароль
            
        Returns:
            str: JWT токен
        """
        user = self.users.get(username)
        if not user or not verify_password(password, user.password_hash):
            raise ValueError('Неверное имя пользователя или пароль')
        
        return generate_jwt(
            {
                'username': user.username,
                'roles': user.roles
            },
            self.secret
        )
    
    def authorize(self, token: str, required_roles: List[str]) -> bool:
        """
        Авторизация пользователя.
        
        Args:
            token (str): JWT токен
            required_roles (List[str]): Требуемые роли
            
        Returns:
            bool: Результат авторизации
        """
        try:
            payload = verify_jwt(token, self.secret)
            user_roles = payload.get('roles', [])
            return any(role in user_roles for role in required_roles)
        except Exception:
            return False


def main():
    """
    Основная функция.
    """
    # Хеширование паролей
    password = 'password123'
    hashed, salt = hash_password(password)
    print('Хеш пароля:', hashed)
    print('Соль:', salt)
    print('Верификация пароля:', verify_password(password, hashed))
    
    # Шифрование данных
    key = generate_key()
    data = 'Секретные данные'
    encrypted = encrypt_data(data, key)
    print('Зашифрованные данные:', encrypted)
    decrypted = decrypt_data(encrypted, key)
    print('Расшифрованные данные:', decrypted)
    
    # Генерация токенов
    payload = {'user_id': 1, 'username': 'john'}
    secret = 'your-secret-key'
    token = generate_jwt(payload, secret)
    print('JWT токен:', token)
    verified_payload = verify_jwt(token, secret)
    print('Верифицированные данные:', verified_payload)
    
    # Работа с SSL/TLS
    private_key, public_key = generate_rsa_key_pair()
    data = 'Данные для подписи'
    signature = sign_data(data, private_key)
    print('Подпись:', base64.b64encode(signature).decode())
    print('Верификация подписи:', verify_signature(data, signature, public_key))
    
    # Безопасное хранение данных
    sensitive_data = '1234567890'
    masked = mask_sensitive_data(sensitive_data)
    print('Замаскированные данные:', masked)
    
    data = {
        'name': 'John Doe',
        'email': 'john@example.com',
        'phone': '1234567890'
    }
    anonymized = anonymize_data(data, ['email', 'phone'])
    print('Анонимизированные данные:', anonymized)
    
    # Аутентификация и авторизация
    auth_service = AuthService(secret)
    auth_service.register_user('john', 'password123', ['user', 'admin'])
    
    token = auth_service.authenticate('john', 'password123')
    print('Токен аутентификации:', token)
    
    is_authorized = auth_service.authorize(token, ['admin'])
    print('Авторизация:', is_authorized)


if __name__ == '__main__':
    main() 
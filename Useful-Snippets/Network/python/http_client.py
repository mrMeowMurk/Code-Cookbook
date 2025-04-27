#!/usr/bin/env python3
"""
Примеры работы с HTTP клиентом в Python.

Этот скрипт демонстрирует различные операции с HTTP:
- GET/POST запросы
- Загрузка файлов
- Отправка файлов
- Работа с заголовками
- Работа с cookies
- Асинхронные запросы
"""

import os
import json
import asyncio
import aiohttp
import requests
from typing import Dict, Any, Optional
from urllib.parse import urljoin


class HTTPClient:
    """
    HTTP клиент.
    """
    def __init__(self, base_url: str):
        """
        Инициализация клиента.
        
        Args:
            base_url (str): Базовый URL
        """
        self.base_url = base_url
        self.session = requests.Session()
    
    def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> requests.Response:
        """
        Выполнение GET запроса.
        
        Args:
            path (str): Путь
            params (Optional[Dict[str, Any]]): Параметры запроса
            
        Returns:
            requests.Response: Ответ
        """
        url = urljoin(self.base_url, path)
        return self.session.get(url, params=params)
    
    def post(self, path: str, data: Optional[Dict[str, Any]] = None, json_data: Optional[Dict[str, Any]] = None) -> requests.Response:
        """
        Выполнение POST запроса.
        
        Args:
            path (str): Путь
            data (Optional[Dict[str, Any]]): Данные формы
            json_data (Optional[Dict[str, Any]]): JSON данные
            
        Returns:
            requests.Response: Ответ
        """
        url = urljoin(self.base_url, path)
        return self.session.post(url, data=data, json=json_data)
    
    def download_file(self, path: str, local_path: str) -> None:
        """
        Загрузка файла.
        
        Args:
            path (str): Путь к файлу на сервере
            local_path (str): Локальный путь для сохранения
        """
        url = urljoin(self.base_url, path)
        response = self.session.get(url, stream=True)
        response.raise_for_status()
        
        with open(local_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
    
    def upload_file(self, path: str, local_path: str) -> requests.Response:
        """
        Отправка файла.
        
        Args:
            path (str): Путь на сервере
            local_path (str): Локальный путь к файлу
            
        Returns:
            requests.Response: Ответ
        """
        url = urljoin(self.base_url, path)
        with open(local_path, 'rb') as file:
            return self.session.post(url, files={'file': file})
    
    def set_headers(self, headers: Dict[str, str]) -> None:
        """
        Установка заголовков.
        
        Args:
            headers (Dict[str, str]): Заголовки
        """
        self.session.headers.update(headers)
    
    def set_cookies(self, cookies: Dict[str, str]) -> None:
        """
        Установка cookies.
        
        Args:
            cookies (Dict[str, str]): Cookies
        """
        self.session.cookies.update(cookies)
    
    def close(self) -> None:
        """
        Закрытие сессии.
        """
        self.session.close()


class AsyncHTTPClient:
    """
    Асинхронный HTTP клиент.
    """
    def __init__(self, base_url: str):
        """
        Инициализация клиента.
        
        Args:
            base_url (str): Базовый URL
        """
        self.base_url = base_url
    
    async def __aenter__(self):
        """
        Вход в контекстный менеджер.
        
        Returns:
            AsyncHTTPClient: Клиент
        """
        self.session = aiohttp.ClientSession()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        Выход из контекстного менеджера.
        """
        await self.session.close()
    
    async def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> aiohttp.ClientResponse:
        """
        Выполнение GET запроса.
        
        Args:
            path (str): Путь
            params (Optional[Dict[str, Any]]): Параметры запроса
            
        Returns:
            aiohttp.ClientResponse: Ответ
        """
        url = urljoin(self.base_url, path)
        return await self.session.get(url, params=params)
    
    async def post(self, path: str, data: Optional[Dict[str, Any]] = None, json_data: Optional[Dict[str, Any]] = None) -> aiohttp.ClientResponse:
        """
        Выполнение POST запроса.
        
        Args:
            path (str): Путь
            data (Optional[Dict[str, Any]]): Данные формы
            json_data (Optional[Dict[str, Any]]): JSON данные
            
        Returns:
            aiohttp.ClientResponse: Ответ
        """
        url = urljoin(self.base_url, path)
        return await self.session.post(url, data=data, json=json_data)
    
    async def download_file(self, path: str, local_path: str) -> None:
        """
        Загрузка файла.
        
        Args:
            path (str): Путь к файлу на сервере
            local_path (str): Локальный путь для сохранения
        """
        url = urljoin(self.base_url, path)
        async with self.session.get(url) as response:
            response.raise_for_status()
            
            with open(local_path, 'wb') as file:
                while True:
                    chunk = await response.content.read(8192)
                    if not chunk:
                        break
                    file.write(chunk)
    
    async def upload_file(self, path: str, local_path: str) -> aiohttp.ClientResponse:
        """
        Отправка файла.
        
        Args:
            path (str): Путь на сервере
            local_path (str): Локальный путь к файлу
            
        Returns:
            aiohttp.ClientResponse: Ответ
        """
        url = urljoin(self.base_url, path)
        with open(local_path, 'rb') as file:
            data = aiohttp.FormData()
            data.add_field('file', file)
            return await self.session.post(url, data=data)


async def main():
    """
    Основная функция.
    """
    # Синхронный клиент
    client = HTTPClient('https://api.example.com')
    
    # GET запрос
    response = client.get('/users', params={'page': 1})
    print('GET ответ:', response.json())
    
    # POST запрос
    response = client.post('/users', json_data={'name': 'John', 'email': 'john@example.com'})
    print('POST ответ:', response.json())
    
    # Загрузка файла
    client.download_file('/files/test.txt', 'test.txt')
    
    # Отправка файла
    response = client.upload_file('/upload', 'test.txt')
    print('Upload ответ:', response.json())
    
    # Установка заголовков
    client.set_headers({'Authorization': 'Bearer token'})
    
    # Установка cookies
    client.set_cookies({'session_id': '123'})
    
    # Закрытие сессии
    client.close()
    
    # Асинхронный клиент
    async with AsyncHTTPClient('https://api.example.com') as client:
        # GET запрос
        response = await client.get('/users', params={'page': 1})
        print('Async GET ответ:', await response.json())
        
        # POST запрос
        response = await client.post('/users', json_data={'name': 'John', 'email': 'john@example.com'})
        print('Async POST ответ:', await response.json())
        
        # Загрузка файла
        await client.download_file('/files/test.txt', 'test.txt')
        
        # Отправка файла
        response = await client.upload_file('/upload', 'test.txt')
        print('Async Upload ответ:', await response.json())
    
    # Очистка
    if os.path.exists('test.txt'):
        os.remove('test.txt')


if __name__ == '__main__':
    asyncio.run(main()) 
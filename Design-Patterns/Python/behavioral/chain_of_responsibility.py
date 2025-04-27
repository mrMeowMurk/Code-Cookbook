"""
Паттерн Chain of Responsibility (Цепочка обязанностей)

Паттерн Chain of Responsibility позволяет передавать запросы по цепочке обработчиков,
где каждый обработчик решает, может ли он обработать запрос, и передает его дальше,
если не может.

Применение:
- Когда нужно обработать запрос несколькими объектами
- Когда нужно реализовать механизм обработки запросов
- Когда нужно реализовать механизм фильтрации запросов
- Когда нужно реализовать механизм маршрутизации запросов

Преимущества:
+ Уменьшает связанность между отправителем и получателем
+ Упрощает добавление новых обработчиков
+ Упрощает тестирование
+ Соблюдает принцип единственной ответственности

Недостатки:
- Может быть сложно отладить
- Может быть сложно реализовать для сложных цепочек
- Может быть сложно контролировать порядок обработки
"""

from abc import ABC, abstractmethod
from typing import Optional


class Handler(ABC):
    """
    Базовый класс обработчика.
    """
    def __init__(self):
        self._next: Optional[Handler] = None

    def set_next(self, handler: 'Handler') -> None:
        """
        Устанавливает следующий обработчик.
        
        Args:
            handler (Handler): Следующий обработчик
        """
        self._next = handler

    def handle_request(self, request: str) -> None:
        """
        Обрабатывает запрос.
        
        Args:
            request (str): Запрос
        """
        if self._next:
            self._next.handle_request(request)


class ConcreteHandlerA(Handler):
    """
    Конкретный обработчик A.
    """
    def handle_request(self, request: str) -> None:
        """
        Обрабатывает запрос.
        
        Args:
            request (str): Запрос
        """
        if request == "A":
            print("Обработчик A обрабатывает запрос")
        else:
            super().handle_request(request)


class ConcreteHandlerB(Handler):
    """
    Конкретный обработчик B.
    """
    def handle_request(self, request: str) -> None:
        """
        Обрабатывает запрос.
        
        Args:
            request (str): Запрос
        """
        if request == "B":
            print("Обработчик B обрабатывает запрос")
        else:
            super().handle_request(request)


class ConcreteHandlerC(Handler):
    """
    Конкретный обработчик C.
    """
    def handle_request(self, request: str) -> None:
        """
        Обрабатывает запрос.
        
        Args:
            request (str): Запрос
        """
        if request == "C":
            print("Обработчик C обрабатывает запрос")
        else:
            super().handle_request(request)


# Пример использования
if __name__ == "__main__":
    # Создаем обработчики
    handler_a = ConcreteHandlerA()
    handler_b = ConcreteHandlerB()
    handler_c = ConcreteHandlerC()

    # Устанавливаем цепочку
    handler_a.set_next(handler_b)
    handler_b.set_next(handler_c)

    # Отправляем запросы
    handler_a.handle_request("A")
    handler_a.handle_request("B")
    handler_a.handle_request("C")
    handler_a.handle_request("D") 
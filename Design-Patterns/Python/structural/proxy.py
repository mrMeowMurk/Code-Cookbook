"""
Паттерн Proxy (Заместитель)

Паттерн Proxy предоставляет суррогат или заместитель для другого объекта,
чтобы контролировать доступ к нему. Он позволяет добавлять дополнительную
функциональность при доступе к объекту.

Применение:
- Когда нужно контролировать доступ к объекту
- Когда нужно добавить дополнительную функциональность при доступе к объекту
- Когда нужно отложить создание объекта до момента его использования
- Когда нужно кэшировать результаты работы объекта

Преимущества:
+ Контролирует доступ к объекту
+ Позволяет добавлять дополнительную функциональность
+ Позволяет отложить создание объекта
+ Позволяет кэшировать результаты

Недостатки:
- Может усложнить код
- Может замедлить работу приложения
- Может быть сложно отладить
"""

from abc import ABC, abstractmethod


class Subject(ABC):
    """
    Базовый класс субъекта.
    """
    @abstractmethod
    def request(self) -> None:
        """Выполняет запрос."""
        pass


class RealSubject(Subject):
    """
    Реальный субъект.
    """
    def request(self) -> None:
        """Выполняет запрос."""
        print("RealSubject: обработка запроса")


class Proxy(Subject):
    """
    Заместитель.
    """
    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    def _check_access(self) -> bool:
        """
        Проверяет доступ.
        
        Returns:
            bool: Результат проверки
        """
        print("Proxy: проверка доступа")
        return True

    def _log_access(self) -> None:
        """Логирует доступ."""
        print("Proxy: логирование доступа")

    def request(self) -> None:
        """Выполняет запрос."""
        if self._check_access():
            self._real_subject.request()
            self._log_access()


def client_code(subject: Subject) -> None:
    """
    Клиентский код.
    
    Args:
        subject (Subject): Субъект
    """
    subject.request()


# Пример использования
if __name__ == "__main__":
    print("Клиент: выполняю запрос напрямую к RealSubject:")
    real_subject = RealSubject()
    client_code(real_subject)
    print()

    print("Клиент: выполняю запрос через Proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy) 
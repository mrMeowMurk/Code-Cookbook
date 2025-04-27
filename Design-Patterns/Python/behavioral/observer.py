"""
Паттерн Observer (Наблюдатель)

Паттерн Observer определяет зависимость "один-ко-многим" между объектами таким образом,
что при изменении состояния одного объекта все зависящие от него объекты автоматически
получают уведомление и обновляются.

Применение:
- Когда нужно реализовать механизм уведомления объектов об изменении состояния
- Когда нужно реализовать механизм подписки на события
- Когда нужно реализовать механизм публикации-подписки
- Когда нужно реализовать механизм обновления зависимых объектов

Преимущества:
+ Уменьшает связанность между объектами
+ Поддерживает принцип слабой связанности
+ Позволяет динамически добавлять и удалять наблюдателей
+ Соблюдает принцип единственной ответственности

Недостатки:
- Может привести к неожиданным обновлениям
- Может быть сложно отладить
- Может быть неэффективным для большого количества наблюдателей
"""

from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):
    """
    Базовый класс наблюдателя.
    """
    @abstractmethod
    def update(self, message: str) -> None:
        """
        Обновляет наблюдателя.
        
        Args:
            message (str): Сообщение
        """
        pass


class Subject:
    """
    Базовый класс субъекта.
    """
    def __init__(self):
        self._observers: List[Observer] = []
        self._message = ""

    def attach(self, observer: Observer) -> None:
        """
        Прикрепляет наблюдателя.
        
        Args:
            observer (Observer): Наблюдатель
        """
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """
        Открепляет наблюдателя.
        
        Args:
            observer (Observer): Наблюдатель
        """
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self) -> None:
        """Уведомляет всех наблюдателей."""
        for observer in self._observers:
            observer.update(self._message)

    def set_message(self, message: str) -> None:
        """
        Устанавливает сообщение.
        
        Args:
            message (str): Сообщение
        """
        self._message = message
        self.notify()


class ConcreteObserver(Observer):
    """
    Конкретный наблюдатель.
    """
    def __init__(self, name: str):
        self._name = name

    def update(self, message: str) -> None:
        """
        Обновляет наблюдателя.
        
        Args:
            message (str): Сообщение
        """
        print(f"Observer {self._name} получил сообщение: {message}")


# Пример использования
if __name__ == "__main__":
    # Создаем субъект
    subject = Subject()

    # Создаем наблюдателей
    observer1 = ConcreteObserver("1")
    observer2 = ConcreteObserver("2")
    observer3 = ConcreteObserver("3")

    # Прикрепляем наблюдателей
    subject.attach(observer1)
    subject.attach(observer2)
    subject.attach(observer3)

    # Отправляем сообщение
    subject.set_message("Привет, мир!")

    # Открепляем одного наблюдателя
    subject.detach(observer2)

    # Отправляем еще одно сообщение
    subject.set_message("Второе сообщение") 
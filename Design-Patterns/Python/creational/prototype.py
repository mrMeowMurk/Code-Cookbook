"""
Паттерн Prototype (Прототип)

Паттерн Prototype позволяет создавать новые объекты путем клонирования существующих,
избегая необходимости создавать объекты с нуля.

Применение:
- Когда система должна быть независима от того, как создаются, компонуются и представляются продукты
- Когда инстанцируемые классы определяются во время выполнения
- Когда создание объекта является дорогостоящим
- Когда нужно избежать построения иерархий фабричных классов

Преимущества:
+ Скрывает сложность создания новых объектов
+ Уменьшает количество подклассов
+ Позволяет добавлять и удалять продукты во время выполнения
+ Уменьшает инициализацию объектов

Недостатки:
- Может быть сложно реализовать клонирование сложных объектов
- Может потребоваться инициализация клонированных объектов
"""

from abc import ABC, abstractmethod
from copy import deepcopy
from typing import Dict, Any


class Prototype(ABC):
    """
    Абстрактный класс прототипа.
    Определяет интерфейс для клонирования объектов.
    """
    @abstractmethod
    def clone(self) -> 'Prototype':
        """Создает клон объекта."""
        pass

    @abstractmethod
    def print_info(self) -> None:
        """Выводит информацию об объекте."""
        pass


class ConcretePrototype(Prototype):
    """
    Конкретный класс прототипа.
    Реализует операцию клонирования.
    """
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

    def clone(self) -> 'ConcretePrototype':
        """
        Создает глубокую копию объекта.
        
        Returns:
            ConcretePrototype: Клон объекта
        """
        return deepcopy(self)

    def print_info(self) -> None:
        """Выводит информацию об объекте."""
        print(f"ConcretePrototype: {self.name}, value: {self.value}")


class PrototypeRegistry:
    """
    Реестр прототипов.
    Хранит и управляет прототипами.
    """
    def __init__(self):
        self._prototype = None

    def set_prototype(self, prototype: Prototype) -> None:
        """
        Устанавливает прототип.
        
        Args:
            prototype (Prototype): Прототип для установки
        """
        self._prototype = prototype

    def create_clone(self) -> Prototype:
        """
        Создает клон текущего прототипа.
        
        Returns:
            Prototype: Клон прототипа или None, если прототип не установлен
        """
        if self._prototype:
            return self._prototype.clone()
        return None


# Пример использования
if __name__ == "__main__":
    # Создаем реестр прототипов
    registry = PrototypeRegistry()

    # Создаем и устанавливаем прототип
    prototype = ConcretePrototype("Original", 42)
    registry.set_prototype(prototype)

    # Создаем клоны
    clone1 = registry.create_clone()
    clone2 = registry.create_clone()

    # Выводим информацию о прототипах
    print("Original prototype:")
    registry.create_clone().print_info()

    print("\nFirst clone:")
    clone1.print_info()

    print("\nSecond clone:")
    clone2.print_info() 
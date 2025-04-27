"""
Паттерн Iterator (Итератор)

Паттерн Iterator предоставляет способ последовательного доступа к элементам
составного объекта без раскрытия его внутреннего представления.

Применение:
- Когда нужно предоставить единый интерфейс для обхода различных структур данных
- Когда нужно скрыть внутреннее представление составного объекта
- Когда нужно поддерживать несколько способов обхода составного объекта
- Когда нужно предоставить единый интерфейс для обхода различных структур данных

Преимущества:
+ Упрощает интерфейс составного объекта
+ Поддерживает различные способы обхода составного объекта
+ Позволяет одновременно обходить составной объект
+ Соблюдает принцип единственной ответственности

Недостатки:
- Может быть избыточным для простых структур данных
- Может быть сложно реализовать для сложных структур данных
- Может быть неэффективным для некоторых структур данных
"""

from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic

T = TypeVar('T')


class Iterator(Generic[T], ABC):
    """
    Базовый класс итератора.
    """
    @abstractmethod
    def next(self) -> T:
        """
        Возвращает следующий элемент.
        
        Returns:
            T: Следующий элемент
        """
        pass

    @abstractmethod
    def has_next(self) -> bool:
        """
        Проверяет, есть ли следующий элемент.
        
        Returns:
            bool: True, если есть следующий элемент, иначе False
        """
        pass


class Container(Generic[T], ABC):
    """
    Базовый класс контейнера.
    """
    @abstractmethod
    def get_iterator(self) -> Iterator[T]:
        """
        Возвращает итератор.
        
        Returns:
            Iterator[T]: Итератор
        """
        pass


class ConcreteContainer(Container[T]):
    """
    Конкретный контейнер.
    """
    def __init__(self):
        self._items: List[T] = []

    def add_item(self, item: T) -> None:
        """
        Добавляет элемент.
        
        Args:
            item (T): Элемент
        """
        self._items.append(item)

    def get_iterator(self) -> Iterator[T]:
        """
        Возвращает итератор.
        
        Returns:
            Iterator[T]: Итератор
        """
        return ConcreteIterator(self._items)


class ConcreteIterator(Iterator[T]):
    """
    Конкретный итератор.
    """
    def __init__(self, items: List[T]):
        self._items = items
        self._position = 0

    def next(self) -> T:
        """
        Возвращает следующий элемент.
        
        Returns:
            T: Следующий элемент
        """
        if self.has_next():
            item = self._items[self._position]
            self._position += 1
            return item
        raise StopIteration("No more items")

    def has_next(self) -> bool:
        """
        Проверяет, есть ли следующий элемент.
        
        Returns:
            bool: True, если есть следующий элемент, иначе False
        """
        return self._position < len(self._items)


# Пример использования
if __name__ == "__main__":
    # Создаем контейнер
    container = ConcreteContainer[str]()
    container.add_item("Item 1")
    container.add_item("Item 2")
    container.add_item("Item 3")

    # Получаем итератор
    iterator = container.get_iterator()

    # Итерируемся по элементам
    print("Итерация по элементам:")
    while iterator.has_next():
        print(iterator.next()) 
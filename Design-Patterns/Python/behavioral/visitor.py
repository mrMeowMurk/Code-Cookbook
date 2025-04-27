"""
Паттерн Visitor (Посетитель)

Паттерн Visitor позволяет определить новую операцию над объектами, не изменяя их классов.
Посетитель инкапсулирует операцию в отдельном объекте, что позволяет добавлять новые
операции без изменения классов объектов.

Применение:
- Когда нужно выполнить операцию над всеми элементами сложной структуры объектов
- Когда нужно добавить новую операцию без изменения классов объектов
- Когда нужно отделить алгоритм от структуры объектов
- Когда нужно реализовать двойную диспетчеризацию

Преимущества:
+ Упрощает добавление новых операций
+ Уменьшает связанность между классами
+ Упрощает тестирование
+ Соблюдает принцип единственной ответственности

Недостатки:
- Может привести к нарушению инкапсуляции
- Может быть сложно отладить
- Может быть сложно реализовать для сложных структур
"""

from abc import ABC, abstractmethod
from typing import List


class Visitor(ABC):
    """
    Базовый класс посетителя.
    """
    @abstractmethod
    def visit_concrete_element_a(self, element: 'ConcreteElementA') -> None:
        """
        Посещает элемент A.
        
        Args:
            element (ConcreteElementA): Элемент A
        """
        pass

    @abstractmethod
    def visit_concrete_element_b(self, element: 'ConcreteElementB') -> None:
        """
        Посещает элемент B.
        
        Args:
            element (ConcreteElementB): Элемент B
        """
        pass


class Element(ABC):
    """
    Базовый класс элемента.
    """
    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        """
        Принимает посетителя.
        
        Args:
            visitor (Visitor): Посетитель
        """
        pass


class ConcreteElementA(Element):
    """
    Конкретный элемент A.
    """
    def accept(self, visitor: Visitor) -> None:
        """
        Принимает посетителя.
        
        Args:
            visitor (Visitor): Посетитель
        """
        visitor.visit_concrete_element_a(self)

    def operation_a(self) -> None:
        """
        Операция A.
        """
        print("Операция A")


class ConcreteElementB(Element):
    """
    Конкретный элемент B.
    """
    def accept(self, visitor: Visitor) -> None:
        """
        Принимает посетителя.
        
        Args:
            visitor (Visitor): Посетитель
        """
        visitor.visit_concrete_element_b(self)

    def operation_b(self) -> None:
        """
        Операция B.
        """
        print("Операция B")


class ConcreteVisitor(Visitor):
    """
    Конкретный посетитель.
    """
    def visit_concrete_element_a(self, element: ConcreteElementA) -> None:
        """
        Посещает элемент A.
        
        Args:
            element (ConcreteElementA): Элемент A
        """
        print("Посетитель посещает элемент A")
        element.operation_a()

    def visit_concrete_element_b(self, element: ConcreteElementB) -> None:
        """
        Посещает элемент B.
        
        Args:
            element (ConcreteElementB): Элемент B
        """
        print("Посетитель посещает элемент B")
        element.operation_b()


class ObjectStructure:
    """
    Структура объектов.
    """
    def __init__(self):
        self._elements: List[Element] = []

    def attach(self, element: Element) -> None:
        """
        Добавляет элемент.
        
        Args:
            element (Element): Элемент
        """
        self._elements.append(element)

    def detach(self, element: Element) -> None:
        """
        Удаляет элемент.
        
        Args:
            element (Element): Элемент
        """
        if element in self._elements:
            self._elements.remove(element)

    def accept(self, visitor: Visitor) -> None:
        """
        Принимает посетителя.
        
        Args:
            visitor (Visitor): Посетитель
        """
        for element in self._elements:
            element.accept(visitor)


# Пример использования
if __name__ == "__main__":
    # Создаем структуру объектов
    object_structure = ObjectStructure()

    # Создаем элементы
    element_a = ConcreteElementA()
    element_b = ConcreteElementB()

    # Добавляем элементы в структуру
    object_structure.attach(element_a)
    object_structure.attach(element_b)

    # Создаем посетителя
    visitor = ConcreteVisitor()

    # Посетитель посещает все элементы
    object_structure.accept(visitor) 
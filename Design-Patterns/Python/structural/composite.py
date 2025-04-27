"""
Паттерн Composite (Компоновщик)

Паттерн Composite позволяет сгруппировать объекты в древовидную структуру
и работать с ними как с единым объектом. Он позволяет клиентам единообразно
работать с отдельными объектами и их композициями.

Применение:
- Когда вы хотите представить иерархию объектов
- Когда клиенты должны единообразно работать с составными и отдельными объектами
- Когда вы хотите упростить работу с деревьями объектов
- Когда вы хотите добавить новые типы компонентов в существующую структуру

Преимущества:
+ Упрощает работу с деревьями объектов
+ Облегчает добавление новых типов компонентов
+ Обеспечивает единообразный интерфейс для клиентов
+ Упрощает клиентский код

Недостатки:
- Может сделать дизайн слишком общим
- Может быть сложно ограничить типы компонентов в композиции
- Может привести к слишком общему интерфейсу
"""

from abc import ABC, abstractmethod
from typing import List, Optional


class Component(ABC):
    """
    Базовый класс компонента.
    """
    @abstractmethod
    def operation(self) -> None:
        """Выполняет операцию."""
        pass

    def add(self, component: 'Component') -> None:
        """
        Добавляет дочерний компонент.
        
        Args:
            component (Component): Дочерний компонент
        """
        pass

    def remove(self, component: 'Component') -> None:
        """
        Удаляет дочерний компонент.
        
        Args:
            component (Component): Дочерний компонент
        """
        pass

    def get_child(self, index: int) -> Optional['Component']:
        """
        Получает дочерний компонент по индексу.
        
        Args:
            index (int): Индекс дочернего компонента
            
        Returns:
            Optional[Component]: Дочерний компонент или None
        """
        return None


class Leaf(Component):
    """
    Конечный компонент, не имеющий дочерних элементов.
    """
    def __init__(self, name: str):
        self.name = name

    def operation(self) -> None:
        """Выполняет операцию."""
        print(f"Leaf: {self.name} выполняет операцию")


class Composite(Component):
    """
    Составной компонент, содержащий дочерние элементы.
    """
    def __init__(self, name: str):
        self.name = name
        self.children: List[Component] = []

    def operation(self) -> None:
        """Выполняет операцию."""
        print(f"Composite: {self.name} выполняет операцию")
        for child in self.children:
            child.operation()

    def add(self, component: Component) -> None:
        """
        Добавляет дочерний компонент.
        
        Args:
            component (Component): Дочерний компонент
        """
        self.children.append(component)

    def remove(self, component: Component) -> None:
        """
        Удаляет дочерний компонент.
        
        Args:
            component (Component): Дочерний компонент
        """
        if component in self.children:
            self.children.remove(component)

    def get_child(self, index: int) -> Optional[Component]:
        """
        Получает дочерний компонент по индексу.
        
        Args:
            index (int): Индекс дочернего компонента
            
        Returns:
            Optional[Component]: Дочерний компонент или None
        """
        if 0 <= index < len(self.children):
            return self.children[index]
        return None


def client_code(component: Component) -> None:
    """
    Клиентский код.
    
    Args:
        component (Component): Компонент
    """
    component.operation()


# Пример использования
if __name__ == "__main__":
    # Создаем дерево компонентов
    tree = Composite("Дерево")
    
    branch1 = Composite("Ветка 1")
    branch2 = Composite("Ветка 2")
    
    leaf1 = Leaf("Лист 1")
    leaf2 = Leaf("Лист 2")
    leaf3 = Leaf("Лист 3")
    
    # Строим дерево
    branch1.add(leaf1)
    branch1.add(leaf2)
    branch2.add(leaf3)
    
    tree.add(branch1)
    tree.add(branch2)
    
    # Выполняем операцию
    print("Выполняем операцию на всем дереве:")
    client_code(tree)
    
    print("\nВыполняем операцию на ветке 1:")
    client_code(branch1) 
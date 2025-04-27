"""
Паттерн Mediator (Посредник)

Паттерн Mediator определяет объект, который инкапсулирует способ взаимодействия
набора объектов. Посредник обеспечивает слабую связанность системы, избавляя
объекты от необходимости явно ссылаться друг на друга.

Применение:
- Когда нужно уменьшить связанность между объектами
- Когда нужно централизовать сложную логику взаимодействия между объектами
- Когда нужно упростить взаимодействие между объектами
- Когда нужно добавить новый способ взаимодействия между объектами

Преимущества:
+ Уменьшает связанность между объектами
+ Централизует сложную логику взаимодействия
+ Упрощает взаимодействие между объектами
+ Соблюдает принцип единственной ответственности

Недостатки:
- Может стать "божественным объектом"
- Может усложнить код
- Может быть сложно отладить
"""

from abc import ABC, abstractmethod
from typing import Optional


class Mediator(ABC):
    """
    Базовый класс посредника.
    """
    @abstractmethod
    def notify(self, sender: 'Component', event: str) -> None:
        """
        Уведомляет посредника о событии.
        
        Args:
            sender (Component): Отправитель
            event (str): Событие
        """
        pass


class Component:
    """
    Базовый класс компонента.
    """
    def __init__(self, mediator: Mediator):
        self._mediator = mediator


class ConcreteMediator(Mediator):
    """
    Конкретный посредник.
    """
    def __init__(self):
        self._component1: Optional[Component1] = None
        self._component2: Optional[Component2] = None

    def set_component1(self, component: 'Component1') -> None:
        """
        Устанавливает компонент 1.
        
        Args:
            component (Component1): Компонент 1
        """
        self._component1 = component

    def set_component2(self, component: 'Component2') -> None:
        """
        Устанавливает компонент 2.
        
        Args:
            component (Component2): Компонент 2
        """
        self._component2 = component

    def notify(self, sender: Component, event: str) -> None:
        """
        Уведомляет посредника о событии.
        
        Args:
            sender (Component): Отправитель
            event (str): Событие
        """
        if event == "A":
            print("Посредник реагирует на A и запускает следующие операции:")
            self._component2.do_c()
        elif event == "D":
            print("Посредник реагирует на D и запускает следующие операции:")
            self._component1.do_b()
            self._component2.do_c()


class Component1(Component):
    """
    Компонент 1.
    """
    def do_a(self) -> None:
        """Выполняет операцию A."""
        print("Компонент 1 выполняет A.")
        self._mediator.notify(self, "A")

    def do_b(self) -> None:
        """Выполняет операцию B."""
        print("Компонент 1 выполняет B.")


class Component2(Component):
    """
    Компонент 2.
    """
    def do_c(self) -> None:
        """Выполняет операцию C."""
        print("Компонент 2 выполняет C.")
        self._mediator.notify(self, "C")

    def do_d(self) -> None:
        """Выполняет операцию D."""
        print("Компонент 2 выполняет D.")
        self._mediator.notify(self, "D")


# Пример использования
if __name__ == "__main__":
    # Создаем посредника
    mediator = ConcreteMediator()

    # Создаем компоненты
    component1 = Component1(mediator)
    component2 = Component2(mediator)

    # Устанавливаем компоненты
    mediator.set_component1(component1)
    mediator.set_component2(component2)

    # Выполняем операции
    component1.do_a()
    print()

    component2.do_d() 
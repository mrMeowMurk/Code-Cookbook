"""
Паттерн Decorator (Декоратор)

Паттерн Decorator позволяет динамически добавлять новую функциональность объектам,
оборачивая их в объекты-декораторы. Это позволяет гибко расширять функциональность
объектов без изменения их исходного кода.

Применение:
- Когда нужно динамически добавлять новые обязанности объектам
- Когда нельзя использовать наследование для расширения функциональности
- Когда нужно добавить функциональность отдельным объектам, а не всему классу
- Когда нужно скрыть детали реализации от клиента

Преимущества:
+ Позволяет динамически добавлять новую функциональность
+ Соблюдает принцип единственной ответственности
+ Соблюдает принцип открытости/закрытости
+ Позволяет комбинировать декораторы

Недостатки:
- Может привести к большому количеству маленьких классов
- Может быть сложно отладить
- Может быть сложно реализовать, если декораторы должны взаимодействовать
"""

from abc import ABC, abstractmethod


class Component(ABC):
    """
    Базовый класс компонента.
    """
    @abstractmethod
    def operation(self) -> str:
        """Выполняет операцию."""
        pass


class ConcreteComponent(Component):
    """
    Конкретный компонент.
    """
    def operation(self) -> str:
        return "ConcreteComponent: базовая операция"


class Decorator(Component):
    """
    Базовый класс декоратора.
    """
    def __init__(self, component: Component):
        self._component = component

    def operation(self) -> str:
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    """
    Конкретный декоратор A.
    """
    def operation(self) -> str:
        return f"ConcreteDecoratorA: ({super().operation()})"


class ConcreteDecoratorB(Decorator):
    """
    Конкретный декоратор B.
    """
    def operation(self) -> str:
        return f"ConcreteDecoratorB: [{super().operation()}]"


def client_code(component: Component) -> None:
    """
    Клиентский код.
    
    Args:
        component (Component): Компонент
    """
    print(f"Результат: {component.operation()}")


# Пример использования
if __name__ == "__main__":
    # Создаем базовый компонент
    simple = ConcreteComponent()
    print("Клиент: У меня есть простой компонент:")
    client_code(simple)
    print()

    # Декорируем компонент
    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("Клиент: Теперь у меня есть декорированный компонент:")
    client_code(decorator2) 
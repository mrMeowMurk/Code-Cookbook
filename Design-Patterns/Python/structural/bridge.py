"""
Паттерн Bridge (Мост)

Паттерн Bridge разделяет абстракцию от её реализации, позволяя им изменяться независимо.
Это позволяет изменять реализацию абстракции без изменения клиентского кода.

Применение:
- Когда вы хотите разделить абстракцию и реализацию
- Когда и абстракция, и реализация могут расширяться через подклассы
- Когда изменения в реализации не должны влиять на клиентский код
- Когда вы хотите скрыть детали реализации от клиента

Преимущества:
+ Разделяет абстракцию и реализацию
+ Улучшает расширяемость
+ Скрывает детали реализации от клиента
+ Позволяет изменять реализацию независимо от абстракции

Недостатки:
- Увеличивает сложность кода
- Может быть избыточным для простых случаев
"""

from abc import ABC, abstractmethod


class Implementation(ABC):
    """
    Абстрактный класс реализации.
    """
    @abstractmethod
    def operation_implementation(self) -> str:
        """Реализация операции."""
        pass


class ConcreteImplementationA(Implementation):
    """
    Конкретная реализация A.
    """
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: результат операции"


class ConcreteImplementationB(Implementation):
    """
    Конкретная реализация B.
    """
    def operation_implementation(self) -> str:
        return "ConcreteImplementationB: результат операции"


class Abstraction:
    """
    Абстрактный класс абстракции.
    """
    def __init__(self, implementation: Implementation):
        self.implementation = implementation

    def operation(self) -> str:
        """
        Базовая операция.
        
        Returns:
            str: Результат операции
        """
        return f"Abstraction: базовая операция с {self.implementation.operation_implementation()}"


class ExtendedAbstraction(Abstraction):
    """
    Расширенная абстракция.
    """
    def operation(self) -> str:
        """
        Расширенная операция.
        
        Returns:
            str: Результат операции
        """
        return f"ExtendedAbstraction: расширенная операция с {self.implementation.operation_implementation()}"


def client_code(abstraction: Abstraction) -> None:
    """
    Клиентский код.
    
    Args:
        abstraction (Abstraction): Абстракция
    """
    print(abstraction.operation())


# Пример использования
if __name__ == "__main__":
    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)
    print()

    implementation2 = ConcreteImplementationB()
    abstraction2 = ExtendedAbstraction(implementation2)
    client_code(abstraction2) 